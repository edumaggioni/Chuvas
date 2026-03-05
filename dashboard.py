"""
Sistema Impacto Climático — Dashboard Analítico
Análise de dados de chuva e desastres naturais no Brasil (2010-2025)
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import sys

# ─── Configuração da página ───────────────────────────────────────────────────
st.set_page_config(
    page_title="Sistema Impacto Climático",
    page_icon="🌧️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CSS Global ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --bg: #0a0e1a;
    --bg2: #0f1629;
    --card: #141b2e;
    --card2: #1a2340;
    --accent: #00d4ff;
    --accent2: #ff6b35;
    --accent3: #7c3aed;
    --danger: #ff4757;
    --warning: #ffa502;
    --success: #2ed573;
    --text: #e8eaf6;
    --muted: #7986a8;
    --border: rgba(0,212,255,0.15);
}

html, body, [class*="css"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif;
}

.stApp { background: var(--bg) !important; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: var(--bg2) !important;
    border-right: 1px solid var(--border);
}
section[data-testid="stSidebar"] * { color: var(--text) !important; }

/* Header */
.sys-header {
    background: linear-gradient(135deg, #0f1629 0%, #1a2340 50%, #0f1629 100%);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px 36px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
}
.sys-header::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(0,212,255,0.08) 0%, transparent 70%);
    pointer-events: none;
}
.sys-header h1 {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: var(--accent) !important;
    margin: 0 0 4px 0;
    letter-spacing: -0.5px;
}
.sys-header p {
    color: var(--muted) !important;
    margin: 0;
    font-size: 0.9rem;
}

/* KPI Cards */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 12px;
    margin-bottom: 28px;
}
.kpi-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 18px 16px;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s;
}
.kpi-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    border-radius: 0 0 12px 12px;
}
.kpi-card.blue::after { background: var(--accent); }
.kpi-card.orange::after { background: var(--accent2); }
.kpi-card.red::after { background: var(--danger); }
.kpi-card.yellow::after { background: var(--warning); }
.kpi-card.purple::after { background: var(--accent3); }
.kpi-card.green::after { background: var(--success); }
.kpi-card.teal::after { background: #00cec9; }

.kpi-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--muted);
    margin-bottom: 8px;
}
.kpi-value {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--text) !important;
    line-height: 1;
}
.kpi-icon {
    font-size: 1.4rem;
    opacity: 0.7;
    position: absolute;
    top: 16px; right: 16px;
}

/* Section titles */
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: var(--accent) !important;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin: 0 0 16px 0;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
}

/* Chart containers */
.chart-box {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}

/* Ranking table */
.ranking-table {
    width: 100%;
    border-collapse: collapse;
}
.ranking-table th {
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--muted) !important;
    padding: 8px 12px;
    border-bottom: 1px solid var(--border);
    text-align: left;
}
.ranking-table td {
    padding: 10px 12px;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    font-size: 0.85rem;
    color: var(--text) !important;
}
.ranking-table tr:last-child td { border-bottom: none; }
.rank-num {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    color: var(--accent) !important;
    font-size: 0.85rem;
}
.rank-bar {
    height: 6px;
    background: var(--card2);
    border-radius: 3px;
    overflow: hidden;
}
.rank-bar-fill {
    height: 100%;
    border-radius: 3px;
    background: linear-gradient(90deg, var(--accent), var(--accent3));
}

/* Severity badges */
.badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.5px;
}
.badge-red { background: rgba(255,71,87,0.2); color: #ff4757; }
.badge-orange { background: rgba(255,107,53,0.2); color: #ff6b35; }
.badge-yellow { background: rgba(255,165,2,0.2); color: #ffa502; }
.badge-blue { background: rgba(0,212,255,0.2); color: #00d4ff; }

/* Correlation info */
.corr-box {
    background: var(--card2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px;
    text-align: center;
}
.corr-value {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: var(--accent) !important;
}
.corr-label {
    font-size: 0.75rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem !important; max-width: 100% !important; }
div[data-testid="stDecoration"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ─── Carregamento de dados ─────────────────────────────────────────────────────
@st.cache_data
def carregar_dados():
    base = os.path.dirname(os.path.abspath(__file__))
    chuva = pd.read_csv(os.path.join(base, "data", "chuva.csv"), parse_dates=["data"])
    desastres = pd.read_csv(os.path.join(base, "data", "desastres.csv"), parse_dates=["data"])
    combinado = pd.read_csv(os.path.join(base, "data", "eventos_combinados.csv"), parse_dates=["data"])
    return chuva, desastres, combinado

df_chuva, df_desastres, df_combinado = carregar_dados()

MESES_PT = {
    1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril",
    5:"Maio", 6:"Junho", 7:"Julho", 8:"Agosto",
    9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"
}

_AXIS_BASE = dict(gridcolor="rgba(255,255,255,0.05)", zerolinecolor="rgba(255,255,255,0.05)")

PLOT_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans", color="#e8eaf6", size=12),
    margin=dict(l=10, r=10, t=40, b=10),
)

def layout(**kwargs):
    """Mescla PLOT_LAYOUT com eixos padrão e kwargs extras, sem conflitos."""
    xaxis = {**_AXIS_BASE, **kwargs.pop("xaxis", {})}
    yaxis = {**_AXIS_BASE, **kwargs.pop("yaxis", {})}
    return dict(**PLOT_LAYOUT, xaxis=xaxis, yaxis=yaxis, **kwargs)


# ─── Tela de Abertura ─────────────────────────────────────────────────────────
if "iniciado" not in st.session_state:
    st.session_state.iniciado = False

if not st.session_state.iniciado:
    # Pré-calcula totais globais para exibir na abertura
    total_registros  = len(df_chuva)
    total_desastres  = len(df_desastres)
    total_mortos     = int(df_desastres["mortos"].sum())
    total_afetados   = int(df_desastres["pessoas_afetadas"].sum())
    anos_range       = f"{df_chuva['ano'].min()}–{df_chuva['ano'].max()}"
    n_cidades        = df_chuva["municipio"].nunique()

    def fmt_splash(n):
        if n >= 1_000_000: return f"{n/1_000_000:.1f}M"
        if n >= 1_000:     return f"{n/1_000:.0f}k"
        return str(n)

    st.markdown(f"""
    <style>
    /* ── Splash ── */
    .splash-wrap {{
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 40px 20px;
        background: radial-gradient(ellipse at 20% 30%, rgba(0,212,255,0.07) 0%, transparent 55%),
                    radial-gradient(ellipse at 80% 70%, rgba(124,58,237,0.08) 0%, transparent 55%),
                    #0a0e1a;
    }}
    .splash-badge {{
        font-size: 0.65rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #00d4ff;
        border: 1px solid rgba(0,212,255,0.4);
        border-radius: 20px;
        padding: 4px 16px;
        margin-bottom: 28px;
        display: inline-block;
    }}
    .splash-icon {{
        font-size: 5rem;
        line-height: 1;
        margin-bottom: 20px;
        filter: drop-shadow(0 0 24px rgba(0,212,255,0.5));
    }}
    .splash-title {{
        font-family: 'Syne', sans-serif;
        font-size: 3.2rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -1.5px;
        text-align: center;
        line-height: 1.1;
        margin-bottom: 8px;
    }}
    .splash-title span {{ color: #00d4ff; }}
    .splash-sub {{
        font-size: 1rem;
        color: #7986a8;
        text-align: center;
        margin-bottom: 48px;
        max-width: 540px;
        line-height: 1.6;
    }}
    .splash-stats {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
        max-width: 680px;
        width: 100%;
        margin-bottom: 48px;
    }}
    .splash-stat {{
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(0,212,255,0.12);
        border-radius: 14px;
        padding: 20px 16px;
        text-align: center;
    }}
    .splash-stat-val {{
        font-family: 'Syne', sans-serif;
        font-size: 1.9rem;
        font-weight: 800;
        color: #00d4ff;
        line-height: 1;
        margin-bottom: 6px;
    }}
    .splash-stat-lbl {{
        font-size: 0.68rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #7986a8;
    }}
    .splash-features {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        max-width: 680px;
        width: 100%;
        margin-bottom: 48px;
    }}
    .splash-feat {{
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 10px;
        padding: 14px 12px;
        text-align: center;
    }}
    .splash-feat-icon {{ font-size: 1.4rem; margin-bottom: 6px; }}
    .splash-feat-txt {{
        font-size: 0.7rem;
        color: #7986a8;
        line-height: 1.4;
    }}
    .splash-divider {{
        width: 60px;
        height: 2px;
        background: linear-gradient(90deg, #00d4ff, #7c3aed);
        border-radius: 2px;
        margin: 0 auto 48px;
    }}
    .splash-footer {{
        font-size: 0.68rem;
        color: #455570;
        text-align: center;
        margin-top: 12px;
        letter-spacing: 0.5px;
    }}
    </style>

    <div class="splash-wrap">
        <div class="splash-badge">🛰️ &nbsp; Sistema de Monitoramento Climático</div>
        <div class="splash-icon">🌧️</div>
        <div class="splash-title">Impacto <span>Climático</span></div>
        <div class="splash-sub">
            Dashboard analítico de precipitação e desastres naturais no Brasil.<br>
            Dados históricos de {anos_range} · {n_cidades} municípios monitorados.
        </div>

        <div class="splash-stats">
            <div class="splash-stat">
                <div class="splash-stat-val">{fmt_splash(total_registros)}</div>
                <div class="splash-stat-lbl">Registros de Chuva</div>
            </div>
            <div class="splash-stat">
                <div class="splash-stat-val">{fmt_splash(total_desastres)}</div>
                <div class="splash-stat-lbl">Eventos de Desastres</div>
            </div>
            <div class="splash-stat">
                <div class="splash-stat-val">{fmt_splash(total_afetados)}</div>
                <div class="splash-stat-lbl">Pessoas Afetadas</div>
            </div>
        </div>

        <div class="splash-divider"></div>

        <div class="splash-features">
            <div class="splash-feat">
                <div class="splash-feat-icon">📊</div>
                <div class="splash-feat-txt">KPIs &amp; Gráficos interativos</div>
            </div>
            <div class="splash-feat">
                <div class="splash-feat-icon">🗺️</div>
                <div class="splash-feat-txt">Mapa de eventos georreferenciado</div>
            </div>
            <div class="splash-feat">
                <div class="splash-feat-icon">📈</div>
                <div class="splash-feat-txt">Tendências &amp; Correlações</div>
            </div>
            <div class="splash-feat">
                <div class="splash-feat-icon">🏆</div>
                <div class="splash-feat-txt">Rankings por município</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_btn = st.columns([1, 2, 1])[1]
    with col_btn:
        if st.button("▶  Acessar o Dashboard", use_container_width=True, type="primary"):
            st.session_state.iniciado = True
            st.rerun()

    st.markdown("""
    <div class="splash-footer">
        INMET · S2ID · CEMADEN &nbsp;|&nbsp; Dados representativos 2010–2025
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ─── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:16px 0 24px; text-align:center;">
        <div style="font-size:2.5rem">🌧️</div>
        <div style="font-family:'Syne',sans-serif;font-size:1.1rem;font-weight:800;color:#00d4ff;letter-spacing:-0.5px;">Impacto Climático</div>
        <div style="font-size:0.7rem;color:#7986a8;letter-spacing:2px;text-transform:uppercase;">Sistema de Análise</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🗓️ Filtros")

    anos = sorted(df_chuva["ano"].unique(), reverse=True)
    ano_sel = st.selectbox("Ano", anos, index=0)

    meses_disp = [0] + sorted(df_chuva[df_chuva["ano"] == ano_sel]["mes"].unique())
    mes_labels = {0: "Todos os meses"} | {m: MESES_PT[m] for m in meses_disp if m != 0}
    mes_sel = st.selectbox("Mês", list(mes_labels.keys()), format_func=lambda x: mes_labels[x])

    st.markdown("---")
    st.markdown("### 🗺️ Visualização")
    mostrar_mapa = st.checkbox("Exibir mapa interativo", value=True)
    top_n = st.slider("Top N cidades no ranking", 5, 30, 10)

    st.markdown("---")
    st.markdown("""
    <div style="font-size:0.7rem;color:#7986a8;line-height:1.6;">
        <b style="color:#00d4ff;">Fontes de dados</b><br>
        • INMET — Estações meteorológicas<br>
        • S2ID — Sistema Integrado de Desastres<br>
        • CEMADEN — Alertas climáticos<br><br>
        <i>Dados representativos 2010–2025</i>
    </div>
    """, unsafe_allow_html=True)


# ─── Filtragem ────────────────────────────────────────────────────────────────
def filtrar(df):
    mask = df["ano"] == ano_sel
    if mes_sel != 0:
        mask &= df["mes"] == mes_sel
    return df[mask]

chuva_f = filtrar(df_chuva)
desastres_f = filtrar(df_desastres)

periodo_label = f"{MESES_PT.get(mes_sel, 'Ano todo')} / {ano_sel}" if mes_sel else f"Ano {ano_sel}"

# ─── Header ──────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="sys-header">
    <h1>🌧️ Sistema Impacto Climático</h1>
    <p>Análise de precipitação e desastres naturais · Brasil · <b style="color:#00d4ff;">{periodo_label}</b></p>
</div>
""", unsafe_allow_html=True)

# ─── KPIs ─────────────────────────────────────────────────────────────────────
total_chuva = chuva_f["volume_mm"].sum()
max_chuva = chuva_f.groupby("municipio")["volume_mm"].sum().max()
n_desastres = len(desastres_f)
mortos = desastres_f["mortos"].sum()
feridos = desastres_f["feridos"].sum()
desabrigados = desastres_f["desabrigados"].sum()
desalojados = desastres_f["desalojados"].sum()
afetados = desastres_f["pessoas_afetadas"].sum()

def fmt(n):
    if n >= 1_000_000: return f"{n/1_000_000:.1f}M"
    if n >= 1_000: return f"{n/1_000:.1f}k"
    return str(int(n))

st.markdown(f"""
<div class="kpi-grid">
  <div class="kpi-card blue">
    <div class="kpi-icon">🌧️</div>
    <div class="kpi-label">Chuva Acumulada</div>
    <div class="kpi-value">{fmt(total_chuva)}<span style="font-size:0.8rem;color:#7986a8;font-family:'DM Sans'"> mm</span></div>
  </div>
  <div class="kpi-card orange">
    <div class="kpi-icon">⚠️</div>
    <div class="kpi-label">Desastres</div>
    <div class="kpi-value">{n_desastres}</div>
  </div>
  <div class="kpi-card red">
    <div class="kpi-icon">💀</div>
    <div class="kpi-label">Óbitos</div>
    <div class="kpi-value">{fmt(mortos)}</div>
  </div>
  <div class="kpi-card yellow">
    <div class="kpi-icon">🚑</div>
    <div class="kpi-label">Feridos</div>
    <div class="kpi-value">{fmt(feridos)}</div>
  </div>
  <div class="kpi-card purple">
    <div class="kpi-icon">🏠</div>
    <div class="kpi-label">Desabrigados</div>
    <div class="kpi-value">{fmt(desabrigados)}</div>
  </div>
  <div class="kpi-card teal">
    <div class="kpi-icon">🚶</div>
    <div class="kpi-label">Desalojados</div>
    <div class="kpi-value">{fmt(desalojados)}</div>
  </div>
  <div class="kpi-card green">
    <div class="kpi-icon">👥</div>
    <div class="kpi-label">Afetados</div>
    <div class="kpi-value">{fmt(afetados)}</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── Linha 1: Barras + Linha ──────────────────────────────────────────────────
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<p class="section-title">📊 Top Municípios por Chuva</p>', unsafe_allow_html=True)
    top_chuva = (
        chuva_f.groupby(["municipio", "uf"])["volume_mm"]
        .sum().reset_index()
        .sort_values("volume_mm", ascending=False)
        .head(top_n)
    )
    fig_bar = go.Figure(go.Bar(
        x=top_chuva["volume_mm"],
        y=top_chuva["municipio"] + " (" + top_chuva["uf"] + ")",
        orientation="h",
        marker=dict(
            color=top_chuva["volume_mm"],
            colorscale=[[0, "#1a2340"], [0.5, "#7c3aed"], [1, "#00d4ff"]],
            line=dict(width=0),
        ),
        text=top_chuva["volume_mm"].apply(lambda x: f"{x:,.0f} mm"),
        textposition="outside",
        textfont=dict(color="#e8eaf6", size=10),
    ))
    fig_bar.update_layout(layout(
        height=360,
        yaxis=dict(autorange="reversed", gridcolor="rgba(255,255,255,0.04)"),
        xaxis=dict(showgrid=False),
        title=dict(text="Volume total de precipitação (mm)", font=dict(size=11, color="#7986a8")),
    ))
    st.plotly_chart(fig_bar, use_container_width=True, config={"displayModeBar": False})

with col2:
    st.markdown('<p class="section-title">📈 Evolução Temporal da Chuva</p>', unsafe_allow_html=True)

    if mes_sel == 0:
        # Evolução mensal no ano
        evo = chuva_f.groupby("mes")["volume_mm"].sum().reset_index()
        evo["mes_nome"] = evo["mes"].map(MESES_PT)
        x_col, x_label = "mes_nome", "Mês"
    else:
        # Evolução diária no mês
        evo = chuva_f.groupby("data")["volume_mm"].sum().reset_index()
        evo["dia"] = evo["data"].dt.day
        x_col, x_label = "dia", "Dia"

    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(
        x=evo[x_col], y=evo["volume_mm"],
        mode="lines+markers",
        line=dict(color="#00d4ff", width=2.5, shape="spline"),
        marker=dict(color="#00d4ff", size=5),
        fill="tozeroy",
        fillcolor="rgba(0,212,255,0.08)",
        name="Chuva (mm)",
    ))
    # Média
    media = evo["volume_mm"].mean()
    fig_line.add_hline(y=media, line_dash="dash", line_color="rgba(255,107,53,0.6)",
                       annotation_text=f"Média: {media:.0f}mm", annotation_position="top right",
                       annotation_font=dict(color="#ff6b35", size=10))

    fig_line.update_layout(layout(
        height=360,
        xaxis_title=x_label, yaxis_title="Volume (mm)",
        title=dict(text="Precipitação acumulada por período", font=dict(size=11, color="#7986a8")),
    ))
    st.plotly_chart(fig_line, use_container_width=True, config={"displayModeBar": False})

# ─── Linha 2: Correlação + Tipos ──────────────────────────────────────────────
col3, col4, col5 = st.columns([1.2, 0.8, 1])

with col3:
    st.markdown('<p class="section-title">🔗 Correlação: Chuva × Desastres</p>', unsafe_allow_html=True)

    # Agrega por municipio
    c_agg = chuva_f.groupby("municipio")["volume_mm"].sum().reset_index()
    c_agg.columns = ["municipio", "chuva_total"]
    d_agg = desastres_f.groupby("municipio").agg(
        n_desastres=("tipo_desastre", "count"),
        afetados=("pessoas_afetadas", "sum"),
    ).reset_index()
    corr_df = c_agg.merge(d_agg, on="municipio", how="inner")

    if len(corr_df) >= 3:
        coef = corr_df[["chuva_total", "n_desastres"]].corr().iloc[0, 1]
        fig_corr = px.scatter(
            corr_df, x="chuva_total", y="n_desastres",
            size="afetados", color="n_desastres",
            text="municipio",
            color_continuous_scale=[[0, "#1a2340"], [0.5, "#7c3aed"], [1, "#ff6b35"]],
            labels={"chuva_total": "Chuva Total (mm)", "n_desastres": "Nº Desastres"},
            size_max=50,
        )
        fig_corr.update_traces(
            textposition="top center",
            textfont=dict(size=9, color="#e8eaf6"),
            marker=dict(line=dict(width=0)),
        )
        fig_corr.update_layout(layout(
            height=320,
            coloraxis_showscale=False,
            title=dict(text=f"Correlação de Pearson: r = {coef:.3f}", font=dict(size=11, color="#7986a8")),
        ))
        st.plotly_chart(fig_corr, use_container_width=True, config={"displayModeBar": False})

        st.markdown(f"""
        <div class="corr-box">
            <div class="corr-value">r = {coef:.3f}</div>
            <div class="corr-label">Coeficiente de Pearson (chuva × desastres)</div>
            <div style="margin-top:8px;font-size:0.8rem;color:#7986a8;">
                {"Correlação forte positiva" if abs(coef) > 0.7 else "Correlação moderada" if abs(coef) > 0.4 else "Correlação fraca"}
                · Tamanho = pessoas afetadas
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Dados insuficientes para correlação no período selecionado.")

with col4:
    st.markdown('<p class="section-title">🌀 Tipos de Desastre</p>', unsafe_allow_html=True)
    if len(desastres_f) > 0:
        tipos = desastres_f["tipo_desastre"].value_counts().reset_index()
        tipos.columns = ["tipo", "count"]
        fig_pie = go.Figure(go.Pie(
            labels=tipos["tipo"],
            values=tipos["count"],
            hole=0.55,
            marker=dict(colors=["#00d4ff","#7c3aed","#ff6b35","#ffa502","#ff4757","#2ed573","#00cec9","#a29bfe","#fd79a8"]),
            textfont=dict(size=9, color="#e8eaf6"),
            textposition="outside",
        ))
        fig_pie.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="DM Sans", color="#e8eaf6"),
            margin=dict(l=0, r=0, t=30, b=0),
            height=300,
            showlegend=False,
            annotations=[dict(text=f"<b>{n_desastres}</b><br>eventos", x=0.5, y=0.5,
                              font=dict(size=13, color="#e8eaf6", family="Syne"), showarrow=False)],
        )
        st.plotly_chart(fig_pie, use_container_width=True, config={"displayModeBar": False})
    else:
        st.info("Nenhum desastre registrado neste período.")

with col5:
    st.markdown('<p class="section-title">📅 Chuva Mensal Histórica</p>', unsafe_allow_html=True)

    hist_mes = df_chuva.groupby(["ano", "mes"])["volume_mm"].sum().reset_index()

    # Agrega por trimestre × ano e converte para milhares
    TRIMESTRES = {
        1: "T1 Jan–Mar", 2: "T1 Jan–Mar",  3: "T1 Jan–Mar",
        4: "T2 Abr–Jun", 5: "T2 Abr–Jun",  6: "T2 Abr–Jun",
        7: "T3 Jul–Set", 8: "T3 Jul–Set",  9: "T3 Jul–Set",
        10: "T4 Out–Dez", 11: "T4 Out–Dez", 12: "T4 Out–Dez",
    }
    ORDEM_TRIM = ["T1 Jan–Mar", "T2 Abr–Jun", "T3 Jul–Set", "T4 Out–Dez"]
    CORES_TRIM  = ["#00d4ff", "#7c3aed", "#ff6b35", "#2ed573"]

    hist_mes["trimestre"] = hist_mes["mes"].map(TRIMESTRES)
    agg = (
        hist_mes
        .groupby(["ano", "trimestre"])["volume_mm"]
        .sum()
        .reset_index()
    )
    agg["volume_k"] = agg["volume_mm"] / 1000

    anos_ord = sorted(agg["ano"].unique())

    fig_line_hist = go.Figure()

    for i, trim in enumerate(ORDEM_TRIM):
        df_trim = agg[agg["trimestre"] == trim].sort_values("ano")
        cor = CORES_TRIM[i]

        # Linha principal
        fig_line_hist.add_trace(go.Scatter(
            x=df_trim["ano"],
            y=df_trim["volume_k"],
            mode="lines+markers",
            name=trim,
            line=dict(color=cor, width=2, shape="spline"),
            marker=dict(color=cor, size=5, line=dict(width=0)),
            fill="tonexty" if i > 0 else "none",
            fillcolor=f"rgba({int(cor[1:3],16)},{int(cor[3:5],16)},{int(cor[5:7],16)},0.05)",
            hovertemplate=(
                f"<b>{trim}</b><br>"
                "Ano: %{x}<br>"
                "Chuva: %{y:.1f}k mm<extra></extra>"
            ),
        ))

    # Linha de média geral anual (todos trimestres)
    media_anual = agg.groupby("ano")["volume_k"].sum().reset_index()
    media_geral = media_anual["volume_k"].mean()
    fig_line_hist.add_hline(
        y=media_geral / 4,  # média por trimestre
        line_dash="dot",
        line_color="rgba(255,255,255,0.2)",
        annotation_text=f"Média: {media_geral/4:.1f}k",
        annotation_font=dict(size=9, color="#7986a8"),
        annotation_position="top left",
    )

    fig_line_hist.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="DM Sans", color="#e8eaf6", size=10),
        margin=dict(l=10, r=10, t=10, b=10),
        height=330,
        xaxis=dict(
            tickvals=anos_ord,
            ticktext=[str(a) for a in anos_ord],
            tickangle=-45,
            tickfont=dict(size=9),
            gridcolor="rgba(255,255,255,0.05)",
            zerolinecolor="rgba(255,255,255,0.05)",
        ),
        yaxis=dict(
            ticksuffix="k",
            tickfont=dict(size=9),
            gridcolor="rgba(255,255,255,0.05)",
            zerolinecolor="rgba(255,255,255,0.05)",
            title=dict(text="mm (mil)", font=dict(size=9, color="#7986a8")),
        ),
        legend=dict(
            orientation="h",
            x=0, y=-0.28,
            font=dict(size=9, color="#e8eaf6"),
            bgcolor="rgba(0,0,0,0)",
        ),
        hovermode="x unified",
    )
    st.plotly_chart(fig_line_hist, use_container_width=True, config={"displayModeBar": False})

# ─── Ranking ──────────────────────────────────────────────────────────────────
st.markdown('<p class="section-title">🏆 Rankings</p>', unsafe_allow_html=True)
r1, r2, r3 = st.columns(3)

def render_ranking(df_rank, col_val, titulo, icone, cor):
    max_val = df_rank[col_val].max() if len(df_rank) > 0 else 1
    rows = ""
    for i, (_, row) in enumerate(df_rank.iterrows(), 1):
        pct = int(row[col_val] / max_val * 100) if max_val > 0 else 0
        medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"<span class='rank-num'>#{i}</span>"
        rows += f"""
        <tr>
            <td>{medal}</td>
            <td style="font-weight:500">{row['municipio']}<br>
                <span style="font-size:0.7rem;color:#7986a8;">{row.get('uf','')}</span></td>
            <td style="text-align:right;font-family:'Syne',sans-serif;color:{cor};">{fmt(row[col_val])}</td>
            <td style="width:80px">
                <div class="rank-bar"><div class="rank-bar-fill" style="width:{pct}%;background:{cor}"></div></div>
            </td>
        </tr>"""

    return f"""
    <div class="chart-box">
        <div class="section-title">{icone} {titulo}</div>
        <table class="ranking-table">
            <thead><tr>
                <th>#</th><th>Município</th><th style="text-align:right">Total</th><th>Bar</th>
            </tr></thead>
            <tbody>{rows}</tbody>
        </table>
    </div>"""

with r1:
    rank_chuva = (
        chuva_f.groupby(["municipio", "uf"])["volume_mm"].sum()
        .reset_index().sort_values("volume_mm", ascending=False).head(top_n)
    )
    rank_chuva.columns = ["municipio", "uf", "volume_mm"]
    st.markdown(render_ranking(rank_chuva, "volume_mm", "Mais Chuva (mm)", "🌧️", "#00d4ff"), unsafe_allow_html=True)

with r2:
    if len(desastres_f) > 0:
        rank_desastres = (
            desastres_f.groupby(["municipio", "uf"])
            .agg(n=("tipo_desastre", "count")).reset_index()
            .sort_values("n", ascending=False).head(top_n)
        )
        rank_desastres.columns = ["municipio", "uf", "volume_mm"]
        st.markdown(render_ranking(rank_desastres, "volume_mm", "Mais Desastres", "⚠️", "#ff6b35"), unsafe_allow_html=True)
    else:
        st.info("Sem desastres no período.")

with r3:
    if len(desastres_f) > 0:
        rank_afetados = (
            desastres_f.groupby(["municipio", "uf"])["pessoas_afetadas"]
            .sum().reset_index().sort_values("pessoas_afetadas", ascending=False).head(top_n)
        )
        rank_afetados.columns = ["municipio", "uf", "volume_mm"]
        st.markdown(render_ranking(rank_afetados, "volume_mm", "Mais Pessoas Afetadas", "👥", "#7c3aed"), unsafe_allow_html=True)
    else:
        st.info("Sem dados de afetados no período.")

# ─── Mapa Interativo ──────────────────────────────────────────────────────────
if mostrar_mapa:
    st.markdown('<p class="section-title">🗺️ Mapa Interativo de Eventos</p>', unsafe_allow_html=True)

    # Agrega estações
    est_agg = (
        chuva_f.groupby(["estacao_nome", "municipio", "uf", "latitude", "longitude"])["volume_mm"]
        .sum().reset_index()
    )
    est_agg["volume_norm"] = (est_agg["volume_mm"] - est_agg["volume_mm"].min()) / \
                              (est_agg["volume_mm"].max() - est_agg["volume_mm"].min() + 1)

    fig_map = go.Figure()

    # Estações de chuva (bubble)
    fig_map.add_trace(go.Scattermapbox(
        lat=est_agg["latitude"],
        lon=est_agg["longitude"],
        mode="markers",
        marker=dict(
            size=est_agg["volume_norm"] * 30 + 8,
            color=est_agg["volume_mm"],
            colorscale=[[0, "#1a2340"], [0.4, "#7c3aed"], [1, "#00d4ff"]],
            opacity=0.75,
            colorbar=dict(title=dict(text="mm", font=dict(color="#e8eaf6", size=11)), thickness=10, x=0.02),
        ),
        text=est_agg.apply(lambda r: f"<b>{r['estacao_nome']}</b><br>{r['municipio']}, {r['uf']}<br>Chuva: {r['volume_mm']:,.0f} mm", axis=1),
        hovertemplate="%{text}<extra></extra>",
        name="Estações Meteorológicas",
    ))

    # Desastres
    if len(desastres_f) > 0:
        fig_map.add_trace(go.Scattermapbox(
            lat=desastres_f["latitude"],
            lon=desastres_f["longitude"],
            mode="markers",
            marker=dict(size=10, color="#ff4757", opacity=0.85,
                        symbol="circle"),
            text=desastres_f.apply(
                lambda r: f"<b>⚠️ {r['tipo_desastre']}</b><br>{r['municipio']}, {r['uf']}<br>"
                          f"Data: {r['data'].strftime('%d/%m/%Y')}<br>"
                          f"Mortos: {r['mortos']} | Feridos: {r['feridos']}<br>"
                          f"Desabrigados: {r['desabrigados']:,}<br>"
                          f"Afetados: {r['pessoas_afetadas']:,}", axis=1),
            hovertemplate="%{text}<extra></extra>",
            name="Eventos de Desastre",
        ))

    fig_map.update_layout(
        mapbox=dict(
            style="carto-darkmatter",
            center=dict(lat=-15.78, lon=-47.93),
            zoom=3.5,
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=0, b=0),
        height=480,
        legend=dict(
            bgcolor="rgba(20,27,46,0.9)",
            bordercolor="rgba(0,212,255,0.3)",
            borderwidth=1,
            font=dict(color="#e8eaf6"),
            x=0.01, y=0.99,
        ),
    )
    st.plotly_chart(fig_map, use_container_width=True, config={"displayModeBar": False})

# ─── Análise de Tendência ─────────────────────────────────────────────────────
st.markdown('<p class="section-title">📉 Análise de Tendência Histórica</p>', unsafe_allow_html=True)
t1, t2 = st.columns(2)

with t1:
    anual_chuva = df_chuva.groupby("ano")["volume_mm"].sum().reset_index()
    anual_desastres = df_desastres.groupby("ano").agg(
        n=("tipo_desastre", "count"), afetados=("pessoas_afetadas", "sum")
    ).reset_index()

    fig_tend = make_subplots(specs=[[{"secondary_y": True}]])
    fig_tend.add_trace(go.Bar(
        x=anual_chuva["ano"], y=anual_chuva["volume_mm"],
        name="Chuva total (mm)", marker_color="rgba(0,212,255,0.35)",
        marker_line=dict(color="#00d4ff", width=1),
    ), secondary_y=False)
    fig_tend.add_trace(go.Scatter(
        x=anual_desastres["ano"], y=anual_desastres["n"],
        mode="lines+markers", name="Nº Desastres",
        line=dict(color="#ff6b35", width=2.5),
        marker=dict(size=8, color="#ff6b35"),
    ), secondary_y=True)
    fig_tend.update_layout(
        **PLOT_LAYOUT, height=280,
        title=dict(text="Chuva anual × Número de desastres", font=dict(size=11, color="#7986a8")),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#e8eaf6", size=10)),
        barmode="overlay",
    )
    fig_tend.update_yaxes(title_text="Chuva (mm)", secondary_y=False, gridcolor="rgba(255,255,255,0.05)")
    fig_tend.update_yaxes(title_text="Desastres", secondary_y=True, gridcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_tend, use_container_width=True, config={"displayModeBar": False})

with t2:
    anual_impacto = df_desastres.groupby("ano").agg(
        mortos=("mortos", "sum"),
        desabrigados=("desabrigados", "sum"),
        afetados=("pessoas_afetadas", "sum"),
    ).reset_index()

    fig_imp = go.Figure()
    fig_imp.add_trace(go.Scatter(
        x=anual_impacto["ano"], y=anual_impacto["afetados"],
        mode="lines+markers", name="Afetados",
        line=dict(color="#7c3aed", width=2.5), fill="tozeroy",
        fillcolor="rgba(124,58,237,0.1)", marker=dict(size=7),
    ))
    fig_imp.add_trace(go.Scatter(
        x=anual_impacto["ano"], y=anual_impacto["desabrigados"],
        mode="lines+markers", name="Desabrigados",
        line=dict(color="#ffa502", width=2), marker=dict(size=7),
    ))
    fig_imp.add_trace(go.Scatter(
        x=anual_impacto["ano"], y=anual_impacto["mortos"],
        mode="lines+markers", name="Mortos",
        line=dict(color="#ff4757", width=2), marker=dict(size=7),
    ))
    fig_imp.update_layout(layout(
        height=280,
        title=dict(text="Impacto humano anual", font=dict(size=11, color="#7986a8")),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#e8eaf6", size=10)),
    ))
    st.plotly_chart(fig_imp, use_container_width=True, config={"displayModeBar": False})

# ─── Tabela de Eventos Extremos ───────────────────────────────────────────────
st.markdown('<p class="section-title">🚨 Eventos Climáticos Extremos</p>', unsafe_allow_html=True)

extremos = df_desastres[df_desastres["pessoas_afetadas"] > 500].sort_values("pessoas_afetadas", ascending=False).head(15)
if len(extremos) > 0:
    ext_display = extremos[[
        "data", "municipio", "uf", "tipo_desastre",
        "chuva_acumulada_mm", "mortos", "desabrigados", "pessoas_afetadas"
    ]].copy()
    ext_display["data"] = ext_display["data"].dt.strftime("%d/%m/%Y")
    ext_display.columns = ["Data", "Município", "UF", "Tipo", "Chuva (mm)", "Mortos", "Desabrigados", "Afetados"]
    st.dataframe(ext_display.reset_index(drop=True), use_container_width=True, height=300)

# Footer
st.markdown("""
<div style="text-align:center;padding:32px 0 16px;color:#7986a8;font-size:0.75rem;border-top:1px solid rgba(0,212,255,0.1);margin-top:32px;">
    <b style="color:#00d4ff;">Sistema Impacto Climático</b> · Análise de Precipitação e Desastres Naturais · Brasil 2010–2025<br>
    Dados representativos baseados em padrões climatológicos reais (INMET / S2ID / CEMADEN)
</div>
""", unsafe_allow_html=True)
