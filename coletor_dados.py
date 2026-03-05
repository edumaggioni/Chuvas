"""
Módulo de coleta de dados — Sistema Impacto Climático
Integração com APIs públicas de meteorologia e desastres.
"""
import requests
import pandas as pd
import os
import json
from datetime import datetime, timedelta

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def coletar_chuva_inmet(token: str, data_inicio: str, data_fim: str) -> pd.DataFrame:
    """
    Coleta dados de chuva da API do INMET.
    https://apitempo.inmet.gov.br/
    
    Parâmetros:
        token: Token de acesso INMET
        data_inicio: YYYY-MM-DD
        data_fim: YYYY-MM-DD
    """
    base_url = "https://apitempo.inmet.gov.br"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        # Lista estações
        r = requests.get(f"{base_url}/estacoes/T", headers=headers, timeout=15)
        r.raise_for_status()
        estacoes = r.json()
        
        registros = []
        for est in estacoes[:50]:  # limita para demo
            codigo = est.get("CD_ESTACAO")
            url = f"{base_url}/estacao/dados/{codigo}/{data_inicio}/{data_fim}"
            try:
                resp = requests.get(url, headers=headers, timeout=10)
                if resp.status_code == 200:
                    dados = resp.json()
                    for d in dados:
                        registros.append({
                            "estacao_id": codigo,
                            "estacao_nome": est.get("DC_NOME", ""),
                            "municipio": est.get("DC_NOME", ""),
                            "uf": est.get("SG_ESTADO", ""),
                            "latitude": float(est.get("VL_LATITUDE", 0)),
                            "longitude": float(est.get("VL_LONGITUDE", 0)),
                            "data": d.get("DT_MEDICAO"),
                            "volume_mm": float(d.get("CHUVA", 0) or 0),
                        })
            except Exception:
                continue
        
        df = pd.DataFrame(registros)
        df["data"] = pd.to_datetime(df["data"])
        df["ano"] = df["data"].dt.year
        df["mes"] = df["data"].dt.month
        return df
    
    except Exception as e:
        print(f"[INMET] Erro: {e}")
        return pd.DataFrame()


def coletar_desastres_s2id(token: str = None) -> pd.DataFrame:
    """
    Coleta dados de desastres do S2ID (Sistema Integrado de Informações sobre Desastres).
    https://s2id.mi.gov.br/
    """
    url = "https://s2id.mi.gov.br/paginas/relatorios/api/eventos"
    params = {"format": "json", "limit": 1000}
    
    try:
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        
        r = requests.get(url, params=params, headers=headers, timeout=20)
        r.raise_for_status()
        dados = r.json()
        
        registros = []
        for item in dados.get("results", dados if isinstance(dados, list) else []):
            registros.append({
                "municipio": item.get("municipio", {}).get("nome", ""),
                "uf": item.get("municipio", {}).get("uf", {}).get("sigla", ""),
                "data": item.get("data_evento"),
                "tipo_desastre": item.get("tipologia", {}).get("descricao", ""),
                "mortos": int(item.get("mortos", 0) or 0),
                "feridos": int(item.get("feridos", 0) or 0),
                "desabrigados": int(item.get("desabrigados", 0) or 0),
                "desalojados": int(item.get("desalojados", 0) or 0),
                "pessoas_afetadas": int(item.get("afetados", 0) or 0),
                "casas_destruidas": int(item.get("residencias_destruidas", 0) or 0),
            })
        
        df = pd.DataFrame(registros)
        if len(df) > 0:
            df["data"] = pd.to_datetime(df["data"])
            df["ano"] = df["data"].dt.year
            df["mes"] = df["data"].dt.month
        return df
    
    except Exception as e:
        print(f"[S2ID] Erro: {e}")
        return pd.DataFrame()


def coletar_chuva_cemaden(municipio_id: str = None) -> pd.DataFrame:
    """
    Coleta dados do CEMADEN (Centro Nacional de Monitoramento e Alertas de Desastres Naturais).
    https://sistemas.cemaden.gov.br/apicemaden/
    """
    base_url = "https://sistemas.cemaden.gov.br/apicemaden/v1"
    
    try:
        url = f"{base_url}/pluviometros"
        if municipio_id:
            url += f"?municipio_id={municipio_id}"
        
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        dados = r.json()
        
        registros = []
        for item in dados:
            registros.append({
                "estacao_id": item.get("codEstacao"),
                "estacao_nome": item.get("nomeEstacao", ""),
                "municipio": item.get("municipio", ""),
                "uf": item.get("uf", ""),
                "latitude": item.get("latitude"),
                "longitude": item.get("longitude"),
                "data": item.get("datahora"),
                "volume_mm": float(item.get("valorMedida", 0) or 0),
            })
        
        df = pd.DataFrame(registros)
        if len(df) > 0:
            df["data"] = pd.to_datetime(df["data"])
        return df
    
    except Exception as e:
        print(f"[CEMADEN] Erro: {e}")
        return pd.DataFrame()


def atualizar_dados_locais(df_novo: pd.DataFrame, arquivo: str, chave_dedup: list):
    """Atualiza CSV local eliminando duplicatas."""
    path = os.path.join(DATA_DIR, arquivo)
    os.makedirs(DATA_DIR, exist_ok=True)
    
    if os.path.exists(path):
        df_existente = pd.read_csv(path)
        df_combined = pd.concat([df_existente, df_novo], ignore_index=True)
        df_combined.drop_duplicates(subset=chave_dedup, keep="last", inplace=True)
    else:
        df_combined = df_novo
    
    df_combined.to_csv(path, index=False)
    print(f"✅ {arquivo} atualizado: {len(df_combined):,} registros")
    return df_combined


def executar_coleta(
    token_inmet: str = None,
    token_s2id: str = None,
    data_inicio: str = None,
    data_fim: str = None,
):
    """Executa coleta completa de todas as fontes."""
    if not data_inicio:
        data_inicio = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    if not data_fim:
        data_fim = datetime.now().strftime("%Y-%m-%d")
    
    print(f"\n🔄 Iniciando coleta: {data_inicio} → {data_fim}")
    print("=" * 50)
    
    # Chuva
    if token_inmet:
        print("\n📡 Coletando dados INMET...")
        df_chuva = coletar_chuva_inmet(token_inmet, data_inicio, data_fim)
        if len(df_chuva) > 0:
            atualizar_dados_locais(df_chuva, "chuva.csv", ["estacao_id", "data"])
        else:
            print("⚠️  INMET: nenhum dado coletado")
    else:
        print("⚠️  Token INMET não configurado — usando dados locais")
    
    # Desastres
    print("\n📡 Coletando dados S2ID...")
    df_desastres = coletar_desastres_s2id(token_s2id)
    if len(df_desastres) > 0:
        atualizar_dados_locais(df_desastres, "desastres.csv", ["municipio", "data", "tipo_desastre"])
    else:
        print("⚠️  S2ID: nenhum dado coletado (verifique conectividade ou credenciais)")
    
    print("\n✅ Coleta concluída!")


if __name__ == "__main__":
    # Exemplo de uso:
    # executar_coleta(token_inmet="SEU_TOKEN", data_inicio="2024-01-01")
    print("Módulo de coleta. Use executar_coleta() com as credenciais das APIs.")
    print("Para dados de demonstração, execute: python gerar_dados.py")
