import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="Financial Performance Analytics — NVIDIA vs Intel",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'IBM Plex Sans', sans-serif;
        background-color: #ffffff;
        color: #1a1a1a;
    }
    .main { background-color: #ffffff; }
    .block-container { padding-top: 1.2rem; padding-bottom: 2rem; }

    /* ── Header ── */
    .header-wrap {
        padding: 20px 0 18px 0;
        border-bottom: 1px solid #ececec;
        margin-bottom: 28px;
    }
    .header-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #0f0f0f;
        letter-spacing: -0.4px;
        margin: 0 0 4px 0;
    }
    .header-sub {
        font-size: 0.75rem;
        color: #b0b0b0;
        letter-spacing: 0.5px;
        margin: 0;
    }
    .header-sub span {
        color: #76b900;
        font-weight: 600;
    }
    .header-sub span.blue {
        color: #0071c5;
    }

    /* ── KPI Cards ── */
    .kpi-card {
        background: #ffffff;
        border: 1px solid #e8e8e8;
        border-radius: 10px;
        padding: 18px 20px 16px 20px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        transition: box-shadow 0.2s;
    }
    .kpi-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .kpi-accent-bar {
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        border-radius: 10px 10px 0 0;
    }
    .kpi-label {
        font-size: 0.6rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.4px;
        color: #b8b8b8;
        margin-bottom: 10px;
        margin-top: 2px;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: 700;
        line-height: 1;
        letter-spacing: -1px;
        margin-bottom: 6px;
    }
    .kpi-sub {
        font-size: 0.68rem;
        color: #c0c0c0;
        letter-spacing: 0.2px;
    }
    .kpi-divider {
        height: 1px;
        background: #f4f4f4;
        margin: 6px 0 8px 0;
    }

    /* ── Section titles ── */
    .section-title {
        font-size: 0.62rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #c8c8c8;
        border-bottom: 1px solid #f2f2f2;
        padding-bottom: 8px;
        margin: 28px 0 16px 0;
    }

    /* ── Insight cards ── */
    .insight {
        background: #fafafa;
        border: 1px solid #f0f0f0;
        border-radius: 8px;
        padding: 13px 16px;
        margin-bottom: 10px;
        font-size: 0.82rem;
        color: #444;
        line-height: 1.65;
        border-left: 3px solid #ddd;
    }
    .insight strong { color: #1a1a1a; font-weight: 600; }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        border-bottom: 1px solid #ececec;
        background: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.4px;
        padding: 10px 22px;
        color: #aaa;
        background: transparent;
    }
    .stTabs [aria-selected="true"] {
        color: #0f0f0f !important;
        border-bottom: 2px solid #0f0f0f !important;
        background: transparent !important;
    }

    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Detectar imagens automaticamente ─────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIRS = [
    os.path.join(BASE_DIR, 'images'),
    BASE_DIR,
]

def find_img(filename):
    for d in IMG_DIRS:
        path = os.path.join(d, filename)
        if os.path.exists(path):
            return Image.open(path)
    return None

def show_img(filename):
    img = find_img(filename)
    if img:
        st.image(img, use_container_width=True)
    else:
        st.caption(f"⚠ Imagem não encontrada: {filename}")

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-wrap">
    <div class="header-title">Financial Performance Analytics — Prophet Forecasting · KMeans Clustering · Variance Analysis | NVIDIA vs Intel</div>
    <p class="header-sub">
        2009–2023 &nbsp;·&nbsp;
        <span>NVDA</span> &nbsp;vs&nbsp; <span class="blue">INTC</span> &nbsp;·&nbsp;
        Python · Prophet · Scikit-learn · Pandas &nbsp;·&nbsp;
        Rafael Reghine Munhoz
    </p>
</div>
""", unsafe_allow_html=True)

# ── KPI Cards ─────────────────────────────────────────────────────────────────
cols = st.columns(6)

kpis = [
    ("NVDA Market Cap", "$1T",    "2023 · vs $10B em 2009",   "#76b900"),
    ("INTC Market Cap", "$109B",  "2022 · vs $112B em 2009",  "#0071c5"),
    ("NVDA Crescimento","688%",   "Receita total 2009→2023",  "#76b900"),
    ("INTC Crescimento","80%",    "Receita total 2009→2022",  "#0071c5"),
    ("NVDA Margem Pico","36%",    "Margem líquida em 2022",   "#76b900"),
    ("Inversão",        "2020",   "Ano em que NVDA > INTC",   "#c0712a"),
]

for col, (label, value, sub, color) in zip(cols, kpis):
    with col:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-accent-bar" style="background:{color}"></div>
            <div class="kpi-label">{label}</div>
            <div class="kpi-value" style="color:{color}">{value}</div>
            <div class="kpi-divider"></div>
            <div class="kpi-sub">{sub}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "  NVIDIA  ", "  Intel  ", "  Comparação  ", "  Visão Geral  "
])

# ── ABA 1 — NVIDIA ────────────────────────────────────────────────────────────
with tab1:
    st.markdown('<div class="section-title">Trajetória Financeira 2009–2023</div>', unsafe_allow_html=True)
    show_img('nvda_analysis.png')

    st.markdown('<div class="section-title">Crescimento de Receita Ano a Ano</div>', unsafe_allow_html=True)
    show_img('nvda_yoy.png')

    st.markdown('<div class="section-title">Forecast de Receita — Prophet 2024–2025</div>', unsafe_allow_html=True)
    show_img('forecast_nvidia.png')

    st.markdown('<div class="section-title">Principais Insights</div>', unsafe_allow_html=True)
    for txt in [
        "<strong>Crescimento explosivo:</strong> Receita cresceu +688% entre 2009 e 2023, de US$ 3.4B para US$ 26.9B.",
        "<strong>Market Cap × Receita:</strong> Em 2021 o Market Cap atingiu US$ 735B — crescendo muito mais rápido que a receita, refletindo expectativas do mercado com IA.",
        "<strong>Eficiência operacional:</strong> ROE atingiu 44% em 2019 e margem líquida chegou a 36% em 2022 — níveis excepcionais para o setor de semicondutores.",
        "<strong>Ponto de inflexão:</strong> A partir de 2017, com o boom de GPUs para deep learning, a NVIDIA acelerou de forma consistente e irreversível.",
    ]:
        st.markdown(f'<div class="insight" style="border-left-color:#76b900">{txt}</div>',
                    unsafe_allow_html=True)

# ── ABA 2 — INTEL ─────────────────────────────────────────────────────────────
with tab2:
    st.markdown('<div class="section-title">Trajetória Financeira 2009–2022</div>', unsafe_allow_html=True)
    show_img('intc_analysis.png')

    st.markdown('<div class="section-title">Crescimento de Receita Ano a Ano</div>', unsafe_allow_html=True)
    show_img('intc_yoy.png')

    st.markdown('<div class="section-title">Forecast de Receita — Prophet 2024–2025</div>', unsafe_allow_html=True)
    show_img('forecast_intel.png')

    st.markdown('<div class="section-title">Principais Insights</div>', unsafe_allow_html=True)
    for txt in [
        "<strong>Estagnação de crescimento:</strong> Entre 2011 e 2021, a receita cresceu apenas +46% em 10 anos — média de 4% ao ano.",
        "<strong>Queda abrupta:</strong> Em 2022, a receita caiu -20% — a maior queda do dataset, sinalizando perda estrutural de competitividade.",
        "<strong>Deterioração de indicadores:</strong> ROE caiu de 28% em 2018 para 7.7% em 2022, reflexo direto da perda de eficiência operacional.",
        "<strong>Market Cap estagnado:</strong> Em 2009 valia US$ 112B. Em 2022, US$ 109B — praticamente zero crescimento de valor em 13 anos.",
    ]:
        st.markdown(f'<div class="insight" style="border-left-color:#0071c5">{txt}</div>',
                    unsafe_allow_html=True)

# ── ABA 3 — COMPARAÇÃO ────────────────────────────────────────────────────────
with tab3:
    st.markdown('<div class="section-title">Receita e Market Cap — Lado a Lado</div>', unsafe_allow_html=True)
    show_img('comparacao_receita_marketcap.png')

    st.markdown('<div class="section-title">Indicadores de Eficiência — Margem Líquida, ROE e ROA</div>', unsafe_allow_html=True)
    show_img('comparacao_indicadores.png')

    st.markdown('<div class="section-title">A História da Inversão de Liderança</div>', unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        for txt in [
            "<strong>2009 — Intel dominava:</strong><br>Intel: US$ 112B · NVIDIA: US$ 10B<br>Intel era 11x maior em valor de mercado.",
            "<strong>2020 — O ponto de cruzamento:</strong><br>NVIDIA ultrapassou a Intel em Market Cap pela primeira vez. O mercado precificou o futuro da IA antes do resultado financeiro.",
        ]:
            st.markdown(f'<div class="insight" style="border-left-color:#c0712a">{txt}</div>',
                        unsafe_allow_html=True)
    with col_b:
        for txt in [
            "<strong>2022 — Inversão consolidada:</strong><br>Intel: US$ 109B (-3% vs 2009)<br>NVIDIA: US$ 359B (+3.370% vs 2009)",
            "<strong>2023 — NVIDIA atinge US$ 1 trilhão:</strong><br>Com a explosão da demanda por GPUs para IA generativa, NVIDIA se torna uma das empresas mais valiosas do mundo.",
        ]:
            st.markdown(f'<div class="insight" style="border-left-color:#c0712a">{txt}</div>',
                        unsafe_allow_html=True)

# ── ABA 4 — VISÃO GERAL ───────────────────────────────────────────────────────
with tab4:
    st.markdown('<div class="section-title">Indicadores de Eficiência — Todas as Empresas</div>', unsafe_allow_html=True)
    show_img('heatmap_empresas.png')

    st.markdown('<div class="section-title">Market Cap vs Eficiência — Scatter Plot</div>', unsafe_allow_html=True)
    show_img('scatter_empresas.png')

    st.markdown('<div class="section-title">Clusterização por Perfil Financeiro — KMeans</div>', unsafe_allow_html=True)
    show_img('clusters_empresas.png')

    st.markdown('<div class="section-title">Destaques do Universo Analisado</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    destaques = [
        (c1, "<strong>Maior ROE médio:</strong> Apple com 61.3% — eficiência de capital excepcionalmente acima da média do setor.", "#555"),
        (c2, "<strong>Maior queda de valor:</strong> SHLDQ (Sears) — os dados anteciparam a falência com margens negativas persistentes por múltiplos anos.", "#555"),
        (c3, "<strong>NVIDIA e Intel:</strong> Perfis opostos no mesmo setor — NVIDIA com crescimento acelerado, Intel com estagnação progressiva de indicadores.", "#555"),
    ]
    for col, txt, color in destaques:
        with col:
            st.markdown(f'<div class="insight" style="border-left-color:{color}">{txt}</div>',
                        unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<p style="font-size:0.72rem;color:#d0d0d0;text-align:center;padding:6px 0">
    Financial Performance Analytics — NVIDIA vs Intel (2009–2023) &nbsp;·&nbsp;
    Rafael Reghine Munhoz &nbsp;·&nbsp;
    <a href="https://github.com/reghine" style="color:#c0c0c0;text-decoration:none">GitHub</a>
    &nbsp;·&nbsp;
    <a href="https://linkedin.com/in/rafaelreghine" style="color:#c0c0c0;text-decoration:none">LinkedIn</a>
</p>
""", unsafe_allow_html=True)
