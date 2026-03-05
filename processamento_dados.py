"""
Módulo de processamento e análise estatística — Sistema Impacto Climático
"""
import pandas as pd
import numpy as np
from scipy import stats
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def carregar_dados():
    """Carrega todos os CSVs locais."""
    chuva = pd.read_csv(os.path.join(DATA_DIR, "chuva.csv"), parse_dates=["data"])
    desastres = pd.read_csv(os.path.join(DATA_DIR, "desastres.csv"), parse_dates=["data"])
    return chuva, desastres


def calcular_correlacao(df_chuva: pd.DataFrame, df_desastres: pd.DataFrame) -> dict:
    """Calcula correlação estatística entre chuva e desastres."""
    # Agrega por municipio/mes
    c = df_chuva.groupby(["municipio", "ano", "mes"])["volume_mm"].sum().reset_index()
    d = df_desastres.groupby(["municipio", "ano", "mes"]).agg(
        n_desastres=("tipo_desastre", "count"),
        mortos=("mortos", "sum"),
        afetados=("pessoas_afetadas", "sum"),
    ).reset_index()
    merged = c.merge(d, on=["municipio", "ano", "mes"], how="inner")

    if len(merged) < 5:
        return {"pearson": None, "spearman": None, "pvalor": None}

    pearson_r, pearson_p = stats.pearsonr(merged["volume_mm"], merged["n_desastres"])
    spearman_r, spearman_p = stats.spearmanr(merged["volume_mm"], merged["n_desastres"])

    return {
        "pearson_r": round(pearson_r, 4),
        "pearson_p": round(pearson_p, 6),
        "spearman_r": round(spearman_r, 4),
        "spearman_p": round(spearman_p, 6),
        "n_amostras": len(merged),
        "interpretacao": (
            "Correlação forte positiva" if abs(pearson_r) > 0.7
            else "Correlação moderada" if abs(pearson_r) > 0.4
            else "Correlação fraca"
        ),
    }


def identificar_extremos(df_chuva: pd.DataFrame, percentil: float = 95) -> pd.DataFrame:
    """Identifica eventos climáticos extremos acima do percentil especificado."""
    threshold = df_chuva["volume_mm"].quantile(percentil / 100)
    extremos = df_chuva[df_chuva["volume_mm"] >= threshold].copy()
    extremos["percentil"] = percentil
    extremos["threshold_mm"] = threshold
    extremos = extremos.sort_values("volume_mm", ascending=False)
    return extremos


def ranking_anos_chuvosos(df_chuva: pd.DataFrame) -> pd.DataFrame:
    """Ranking histórico dos anos mais chuvosos."""
    anual = df_chuva.groupby("ano")["volume_mm"].agg(
        total="sum", media_diaria="mean", max_dia="max"
    ).reset_index()
    anual = anual.sort_values("total", ascending=False)
    anual["rank"] = range(1, len(anual) + 1)
    return anual


def analise_tendencia(df_chuva: pd.DataFrame, df_desastres: pd.DataFrame) -> dict:
    """Análise de tendência temporal de chuvas e desastres."""
    anual_c = df_chuva.groupby("ano")["volume_mm"].sum().reset_index()
    anual_d = df_desastres.groupby("ano")["tipo_desastre"].count().reset_index()
    anual_d.columns = ["ano", "n_desastres"]

    # Regressão linear
    if len(anual_c) >= 3:
        slope_c, intercept_c, r_c, p_c, _ = stats.linregress(anual_c["ano"], anual_c["volume_mm"])
        slope_d, intercept_d, r_d, p_d, _ = stats.linregress(
            anual_d["ano"], anual_d["n_desastres"]
        ) if len(anual_d) >= 3 else (None, None, None, None, None)

        return {
            "chuva": {
                "slope_por_ano": round(slope_c, 2),
                "r2": round(r_c ** 2, 4),
                "pvalor": round(p_c, 6),
                "tendencia": "crescente" if slope_c > 0 else "decrescente",
            },
            "desastres": {
                "slope_por_ano": round(slope_d, 2) if slope_d else None,
                "r2": round(r_d ** 2, 4) if r_d else None,
                "pvalor": round(p_d, 6) if p_d else None,
                "tendencia": ("crescente" if slope_d and slope_d > 0 else "decrescente") if slope_d else None,
            },
        }
    return {}


def sazonalidade_media(df_chuva: pd.DataFrame) -> pd.DataFrame:
    """Calcula precipitação média por mês para análise de sazonalidade."""
    sazo = df_chuva.groupby(["municipio", "mes"])["volume_mm"].mean().reset_index()
    sazo.columns = ["municipio", "mes", "media_mm"]
    return sazo


def gerar_relatorio_periodo(df_chuva: pd.DataFrame, df_desastres: pd.DataFrame,
                             ano: int, mes: int = None) -> dict:
    """Gera relatório completo para um período específico."""
    mask_c = df_chuva["ano"] == ano
    mask_d = df_desastres["ano"] == ano
    if mes:
        mask_c &= df_chuva["mes"] == mes
        mask_d &= df_desastres["mes"] == mes

    c = df_chuva[mask_c]
    d = df_desastres[mask_d]

    return {
        "periodo": f"{ano}" + (f"/{mes:02d}" if mes else ""),
        "chuva": {
            "total_mm": round(c["volume_mm"].sum(), 1),
            "media_diaria_mm": round(c["volume_mm"].mean(), 2),
            "max_evento_mm": round(c["volume_mm"].max(), 1),
            "municipio_mais_chuvoso": c.groupby("municipio")["volume_mm"].sum().idxmax() if len(c) > 0 else None,
        },
        "desastres": {
            "total_eventos": len(d),
            "mortos": int(d["mortos"].sum()),
            "feridos": int(d["feridos"].sum()),
            "desabrigados": int(d["desabrigados"].sum()),
            "desalojados": int(d["desalojados"].sum()),
            "afetados": int(d["pessoas_afetadas"].sum()),
            "casas_destruidas": int(d["casas_destruidas"].sum()),
            "tipo_mais_comum": d["tipo_desastre"].mode()[0] if len(d) > 0 else None,
        },
    }


if __name__ == "__main__":
    df_c, df_d = carregar_dados()
    print("\n📊 ANÁLISE ESTATÍSTICA — Sistema Impacto Climático")
    print("=" * 55)

    corr = calcular_correlacao(df_c, df_d)
    print(f"\n🔗 Correlação (Pearson): r = {corr['pearson_r']} | p = {corr['pearson_p']}")
    print(f"   Interpretação: {corr['interpretacao']}")
    print(f"   Amostras: {corr['n_amostras']}")

    anos_rank = ranking_anos_chuvosos(df_c)
    print(f"\n🏆 Ranking anos mais chuvosos:")
    print(anos_rank.head(5).to_string(index=False))

    tend = analise_tendencia(df_c, df_d)
    print(f"\n📉 Tendência de chuva: {tend['chuva']['tendencia']} ({tend['chuva']['slope_por_ano']} mm/ano)")
    if tend["desastres"]["slope_por_ano"]:
        print(f"   Tendência desastres: {tend['desastres']['tendencia']} ({tend['desastres']['slope_por_ano']}/ano)")

    rel = gerar_relatorio_periodo(df_c, df_d, 2022, 2)
    print(f"\n📋 Relatório Petrópolis (fev/2022):")
    for k, v in rel.items():
        print(f"   {k}: {v}")
