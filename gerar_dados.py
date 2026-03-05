"""
Módulo gerador de dados realistas para o Sistema Impacto Climático.
Simula dados de chuva e desastres naturais no Brasil (2019-2024).
"""
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

ESTACOES = [
    {"id": "E001", "nome": "São Paulo - Mirante",          "lat": -23.5489, "lon": -46.6388, "uf": "SP", "municipio": "São Paulo"},
    {"id": "E002", "nome": "Rio de Janeiro - Jacarepaguá", "lat": -22.9899, "lon": -43.3496, "uf": "RJ", "municipio": "Rio de Janeiro"},
    {"id": "E003", "nome": "Belo Horizonte - Pampulha",    "lat": -19.8516, "lon": -43.9704, "uf": "MG", "municipio": "Belo Horizonte"},
    {"id": "E004", "nome": "Salvador - Ondina",            "lat": -13.0078, "lon": -38.5320, "uf": "BA", "municipio": "Salvador"},
    {"id": "E005", "nome": "Recife - Curado",              "lat":  -8.0584, "lon": -34.9286, "uf": "PE", "municipio": "Recife"},
    {"id": "E006", "nome": "Fortaleza - Pici",             "lat":  -3.7480, "lon": -38.5476, "uf": "CE", "municipio": "Fortaleza"},
    {"id": "E007", "nome": "Porto Alegre - Jardim Botânico","lat": -30.0331, "lon": -51.2300, "uf": "RS", "municipio": "Porto Alegre"},
    {"id": "E008", "nome": "Manaus - V8",                  "lat":  -3.1190, "lon": -60.0217, "uf": "AM", "municipio": "Manaus"},
    {"id": "E009", "nome": "Curitiba - São José dos Pinhais","lat":-25.5300, "lon": -49.1731, "uf": "PR", "municipio": "Curitiba"},
    {"id": "E010", "nome": "Belém - Val de Cans",          "lat":  -1.3785, "lon": -48.4760, "uf": "PA", "municipio": "Belém"},
    {"id": "E011", "nome": "Petrópolis - Quitandinha",     "lat": -22.5096, "lon": -43.1796, "uf": "RJ", "municipio": "Petrópolis"},
    {"id": "E012", "nome": "Angra dos Reis - Centro",      "lat": -23.0067, "lon": -44.3181, "uf": "RJ", "municipio": "Angra dos Reis"},
    {"id": "E013", "nome": "Joinville - Pirabeiraba",      "lat": -26.1770, "lon": -48.8520, "uf": "SC", "municipio": "Joinville"},
    {"id": "E014", "nome": "Blumenau - Garcia",            "lat": -26.9195, "lon": -49.0661, "uf": "SC", "municipio": "Blumenau"},
    {"id": "E015", "nome": "Maceió - Tabuleiro",           "lat":  -9.3991, "lon": -36.6321, "uf": "AL", "municipio": "Maceió"},
    {"id": "E016", "nome": "Natal - Augusto Severo",       "lat":  -5.9091, "lon": -35.2478, "uf": "RN", "municipio": "Natal"},
    {"id": "E017", "nome": "Teresina - Parque Lagoas",     "lat":  -5.0892, "lon": -42.8019, "uf": "PI", "municipio": "Teresina"},
    {"id": "E018", "nome": "São Luís - Tirirical",         "lat":  -2.5307, "lon": -44.3068, "uf": "MA", "municipio": "São Luís"},
    {"id": "E019", "nome": "Goiânia - Aeroporto",          "lat": -16.6325, "lon": -49.2201, "uf": "GO", "municipio": "Goiânia"},
    {"id": "E020", "nome": "Brasília - Sudoeste",          "lat": -15.7801, "lon": -47.9292, "uf": "DF", "municipio": "Brasília"},
    {"id": "E021", "nome": "Florianópolis - São José",     "lat": -27.5954, "lon": -48.5480, "uf": "SC", "municipio": "Florianópolis"},
    {"id": "E022", "nome": "Vitória - Goiabeiras",         "lat": -20.3155, "lon": -40.3128, "uf": "ES", "municipio": "Vitória"},
    {"id": "E023", "nome": "Campo Grande - Dom Bosco",     "lat": -20.4697, "lon": -54.6201, "uf": "MS", "municipio": "Campo Grande"},
    {"id": "E024", "nome": "Cuiabá - Várzea Grande",       "lat": -15.6522, "lon": -56.1003, "uf": "MT", "municipio": "Cuiabá"},
    {"id": "E025", "nome": "Macapá - Fazendinha",          "lat":   0.0388, "lon": -51.0664, "uf": "AP", "municipio": "Macapá"},
    {"id": "E026", "nome": "Porto Velho - Belmonte",       "lat":  -8.7619, "lon": -63.8978, "uf": "RO", "municipio": "Porto Velho"},
    {"id": "E027", "nome": "Rio Branco - Aeroporto",       "lat":  -9.9574, "lon": -67.8060, "uf": "AC", "municipio": "Rio Branco"},
    {"id": "E028", "nome": "Boa Vista - Aeroporto",        "lat":   2.8414, "lon": -60.6922, "uf": "RR", "municipio": "Boa Vista"},
    {"id": "E029", "nome": "Nova Friburgo - Campo do Coelho","lat":-22.2823, "lon": -42.5311, "uf": "RJ", "municipio": "Nova Friburgo"},
    {"id": "E030", "nome": "Teresópolis - Alto",           "lat": -22.4125, "lon": -42.9658, "uf": "RJ", "municipio": "Teresópolis"},
]

MUNICIPIOS_DESASTRES = [
    {"municipio": "São Paulo",       "uf": "SP", "lat": -23.5505, "lon": -46.6333},
    {"municipio": "Rio de Janeiro",  "uf": "RJ", "lat": -22.9068, "lon": -43.1729},
    {"municipio": "Belo Horizonte",  "uf": "MG", "lat": -19.9191, "lon": -43.9386},
    {"municipio": "Salvador",        "uf": "BA", "lat": -12.9714, "lon": -38.5014},
    {"municipio": "Recife",          "uf": "PE", "lat":  -8.0476, "lon": -34.8770},
    {"municipio": "Fortaleza",       "uf": "CE", "lat":  -3.7172, "lon": -38.5433},
    {"municipio": "Porto Alegre",    "uf": "RS", "lat": -30.0346, "lon": -51.2177},
    {"municipio": "Manaus",          "uf": "AM", "lat":  -3.1190, "lon": -60.0217},
    {"municipio": "Curitiba",        "uf": "PR", "lat": -25.4284, "lon": -49.2733},
    {"municipio": "Belém",           "uf": "PA", "lat":  -1.4558, "lon": -48.5044},
    {"municipio": "Petrópolis",      "uf": "RJ", "lat": -22.5096, "lon": -43.1796},
    {"municipio": "Angra dos Reis",  "uf": "RJ", "lat": -23.0067, "lon": -44.3181},
    {"municipio": "Joinville",       "uf": "SC", "lat": -26.3044, "lon": -48.8487},
    {"municipio": "Blumenau",        "uf": "SC", "lat": -26.9195, "lon": -49.0661},
    {"municipio": "Maceió",          "uf": "AL", "lat":  -9.6660, "lon": -35.7350},
    {"municipio": "Natal",           "uf": "RN", "lat":  -5.7945, "lon": -35.2110},
    {"municipio": "Teresina",        "uf": "PI", "lat":  -5.0892, "lon": -42.8019},
    {"municipio": "São Luís",        "uf": "MA", "lat":  -2.5307, "lon": -44.3068},
    {"municipio": "Goiânia",         "uf": "GO", "lat": -16.6869, "lon": -49.2648},
    {"municipio": "Brasília",        "uf": "DF", "lat": -15.7801, "lon": -47.9292},
    {"municipio": "Florianópolis",   "uf": "SC", "lat": -27.5954, "lon": -48.5480},
    {"municipio": "Vitória",         "uf": "ES", "lat": -20.3155, "lon": -40.3128},
    {"municipio": "Campo Grande",    "uf": "MS", "lat": -20.4697, "lon": -54.6201},
    {"municipio": "Cuiabá",          "uf": "MT", "lat": -15.6522, "lon": -56.1003},
    {"municipio": "Macapá",          "uf": "AP", "lat":   0.0388, "lon": -51.0664},
    {"municipio": "Porto Velho",     "uf": "RO", "lat":  -8.7619, "lon": -63.8978},
    {"municipio": "Rio Branco",      "uf": "AC", "lat":  -9.9574, "lon": -67.8060},
    {"municipio": "Boa Vista",       "uf": "RR", "lat":   2.8414, "lon": -60.6922},
    {"municipio": "Nova Friburgo",   "uf": "RJ", "lat": -22.2823, "lon": -42.5311},
    {"municipio": "Teresópolis",     "uf": "RJ", "lat": -22.4125, "lon": -42.9658},
]

TIPOS_DESASTRE = [
    "Enxurrada", "Deslizamento de terra", "Enchente", "Alagamento",
    "Tempestade", "Granizo", "Vendaval", "Erosão costeira", "Inundação brusca"
]

# Sazonalidade por UF (meses chuvosos)
SAZONALIDADE = {
    "SP": [11, 12, 1, 2, 3],
    "RJ": [11, 12, 1, 2, 3],
    "MG": [11, 12, 1, 2, 3],
    "BA": [3, 4, 5, 6, 7],
    "PE": [3, 4, 5, 6, 7],
    "CE": [1, 2, 3, 4, 5],
    "RN": [1, 2, 3, 4, 5],
    "PI": [1, 2, 3, 4],
    "MA": [1, 2, 3, 4, 5],
    "RS": [5, 6, 7, 8, 9],
    "AM": [1, 2, 3, 4, 11, 12],
    "PR": [10, 11, 12, 1, 2],
    "PA": [1, 2, 3, 4, 12],
    "SC": [10, 11, 12, 1, 2],
    "AL": [4, 5, 6, 7, 8],
    "GO": [11, 12, 1, 2, 3],
    "DF": [11, 12, 1, 2, 3],
    "ES": [11, 12, 1, 2, 3],
    "MS": [11, 12, 1, 2],
    "MT": [11, 12, 1, 2, 3],
    "AP": [1, 2, 3, 4, 12],
    "RO": [1, 2, 3, 11, 12],
    "AC": [1, 2, 3, 11, 12],
    "RR": [4, 5, 6, 7, 8],
}


def fator_sazonalidade(uf, mes):
    meses_chuvosos = SAZONALIDADE.get(uf, [1, 2, 3, 11, 12])
    if mes in meses_chuvosos:
        return np.random.uniform(1.5, 3.5)
    return np.random.uniform(0.1, 0.8)


def gerar_dados_chuva():
    registros = []
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2025, 12, 31)
    current = start_date

    while current <= end_date:
        for est in ESTACOES:
            fator = fator_sazonalidade(est["uf"], current.month)
            # Volume diário base + sazonalidade + ruído
            volume_base = np.random.exponential(5) * fator
            # Eventos extremos ocasionais
            if np.random.random() < 0.03:
                volume_base *= np.random.uniform(5, 15)
            volume = round(max(0, volume_base), 1)

            registros.append({
                "estacao_id": est["id"],
                "estacao_nome": est["nome"],
                "municipio": est["municipio"],
                "uf": est["uf"],
                "latitude": est["lat"],
                "longitude": est["lon"],
                "data": current.strftime("%Y-%m-%d"),
                "ano": current.year,
                "mes": current.month,
                "volume_mm": volume,
            })
        current += timedelta(days=1)

    df = pd.DataFrame(registros)
    return df


def gerar_dados_desastres(df_chuva):
    registros = []

    # Agrupa chuva por municipio/data
    chuva_mun = df_chuva.groupby(["municipio", "data", "ano", "mes"])["volume_mm"].sum().reset_index()

    for _, row in chuva_mun.iterrows():
        mun_info = next((m for m in MUNICIPIOS_DESASTRES if m["municipio"] == row["municipio"]), None)
        if mun_info is None:
            continue

        # Probabilidade de desastre aumenta com chuva intensa
        threshold = 50
        if row["volume_mm"] > threshold:
            prob = min(0.9, (row["volume_mm"] - threshold) / 200)
            if np.random.random() < prob:
                tipo = random.choice(TIPOS_DESASTRE)
                intensidade = row["volume_mm"] / 50
                mortos = int(np.random.poisson(intensidade * 0.3))
                feridos = int(np.random.poisson(intensidade * 2))
                desabrigados = int(np.random.poisson(intensidade * 15))
                desalojados = int(np.random.poisson(intensidade * 30))
                afetados = desabrigados + desalojados + int(np.random.poisson(intensidade * 50))
                casas_destruidas = int(np.random.poisson(intensidade * 5))

                registros.append({
                    "municipio": row["municipio"],
                    "uf": mun_info["uf"],
                    "latitude": mun_info["lat"],
                    "longitude": mun_info["lon"],
                    "data": row["data"],
                    "ano": row["ano"],
                    "mes": row["mes"],
                    "tipo_desastre": tipo,
                    "mortos": mortos,
                    "feridos": feridos,
                    "desabrigados": desabrigados,
                    "desalojados": desalojados,
                    "pessoas_afetadas": afetados,
                    "casas_destruidas": casas_destruidas,
                    "chuva_acumulada_mm": round(row["volume_mm"], 1),
                })

    df = pd.DataFrame(registros)
    # ── Eventos históricos reais ──────────────────────────────────────────────
    historicos = [
        # Petrópolis fev/2022
        {"municipio": "Petrópolis",    "uf": "RJ", "latitude": -22.5096, "longitude": -43.1796,
         "data": "2022-02-15", "ano": 2022, "mes": 2, "tipo_desastre": "Deslizamento de terra",
         "mortos": 233, "feridos": 400, "desabrigados": 2800, "desalojados": 8000,
         "pessoas_afetadas": 25000, "casas_destruidas": 500, "chuva_acumulada_mm": 258.0},
        # Serrana RJ jan/2011
        {"municipio": "Nova Friburgo", "uf": "RJ", "latitude": -22.2823, "longitude": -42.5311,
         "data": "2011-01-12", "ano": 2011, "mes": 1, "tipo_desastre": "Deslizamento de terra",
         "mortos": 428, "feridos": 300, "desabrigados": 15000, "desalojados": 22000,
         "pessoas_afetadas": 80000, "casas_destruidas": 1500, "chuva_acumulada_mm": 280.0},
        {"municipio": "Teresópolis",   "uf": "RJ", "latitude": -22.4125, "longitude": -42.9658,
         "data": "2011-01-12", "ano": 2011, "mes": 1, "tipo_desastre": "Enxurrada",
         "mortos": 385, "feridos": 250, "desabrigados": 12000, "desalojados": 18000,
         "pessoas_afetadas": 60000, "casas_destruidas": 1200, "chuva_acumulada_mm": 263.0},
        # Rio Grande do Sul mai/2024
        {"municipio": "Porto Alegre",  "uf": "RS", "latitude": -30.0346, "longitude": -51.2177,
         "data": "2024-05-03", "ano": 2024, "mes": 5, "tipo_desastre": "Enchente",
         "mortos": 147, "feridos": 806, "desabrigados": 70000, "desalojados": 380000,
         "pessoas_afetadas": 2300000, "casas_destruidas": 2500, "chuva_acumulada_mm": 320.0},
        {"municipio": "Blumenau",      "uf": "SC", "latitude": -26.9195, "longitude": -49.0661,
         "data": "2023-11-18", "ano": 2023, "mes": 11, "tipo_desastre": "Enxurrada",
         "mortos": 14, "feridos": 45, "desabrigados": 3500, "desalojados": 9000,
         "pessoas_afetadas": 40000, "casas_destruidas": 300, "chuva_acumulada_mm": 198.0},
        # Recife mai/2022
        {"municipio": "Recife",        "uf": "PE", "latitude": -8.0476, "longitude": -34.8770,
         "data": "2022-05-28", "ano": 2022, "mes": 5, "tipo_desastre": "Deslizamento de terra",
         "mortos": 128, "feridos": 320, "desabrigados": 8000, "desalojados": 16000,
         "pessoas_afetadas": 120000, "casas_destruidas": 980, "chuva_acumulada_mm": 233.0},
    ]
    df = pd.concat([df, pd.DataFrame(historicos)], ignore_index=True)
    return df


def salvar_dados():
    os.makedirs("data", exist_ok=True)
    print("⏳ Gerando dados de chuva (2010-2025)...")
    df_chuva = gerar_dados_chuva()
    df_chuva.to_csv("data/chuva.csv", index=False)
    print(f"✅ chuva.csv: {len(df_chuva):,} registros")

    print("⏳ Gerando dados de desastres...")
    df_desastres = gerar_dados_desastres(df_chuva)
    df_desastres.to_csv("data/desastres.csv", index=False)
    print(f"✅ desastres.csv: {len(df_desastres):,} registros")

    print("⏳ Gerando eventos combinados...")
    # Agrega chuva por municipio/data
    chuva_agg = df_chuva.groupby(["municipio", "uf", "latitude", "longitude", "data", "ano", "mes"])["volume_mm"].sum().reset_index()
    chuva_agg.columns = ["municipio", "uf", "latitude", "longitude", "data", "ano", "mes", "chuva_total_mm"]

    df_combined = chuva_agg.merge(
        df_desastres[["municipio", "data", "tipo_desastre", "mortos", "feridos",
                      "desabrigados", "desalojados", "pessoas_afetadas", "casas_destruidas"]],
        on=["municipio", "data"], how="left"
    )
    df_combined.to_csv("data/eventos_combinados.csv", index=False)
    print(f"✅ eventos_combinados.csv: {len(df_combined):,} registros")
    print("\n✅ Dados gerados com sucesso!")
    return df_chuva, df_desastres, df_combined


if __name__ == "__main__":
    salvar_dados()
