import streamlit as st
import requests

# Configuração de página e CSS customizado
st.set_page_config(
    page_title="Star Wars Explorer",
    page_icon="🌌",
    layout="wide"
)

# CSS customizado com tema Star Wars cinematográfico
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&family=Audiowide&display=swap');
    
    /* Background principal */
    .main {
        background: linear-gradient(180deg, #000000 0%, #0a0a1a 50%, #000000 100%);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a1a 0%, #1a1a2e 50%, #0a0a1a 100%);
        border-right: 2px solid #FFE81F;
        box-shadow: 4px 0 20px rgba(255, 232, 31, 0.15);
    }
    
    [data-testid="stSidebar"] * {
        font-family: 'Rajdhani', sans-serif;
    }
    
    /* Títulos */
    h1, h2, h3 {
        font-family: 'Audiowide', cursive;
        color: #FFE81F !important;
        text-shadow: 0 0 20px rgba(255, 232, 31, 0.6);
        letter-spacing: 2px;
    }
    
    /* Radio buttons - navegação */
    .stRadio > label {
        font-family: 'Rajdhani', sans-serif;
        font-size: 16px;
        font-weight: 500;
        color: #a8b2d1 !important;
    }
    
    .stRadio > div {
        background: rgba(26, 26, 46, 0.5);
        border-radius: 10px;
        padding: 10px;
        border: 1px solid rgba(255, 232, 31, 0.2);
    }
    
    .stRadio > div > label {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 8px;
        padding: 12px 16px !important;
        margin: 4px 0;
        border: 1px solid transparent;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .stRadio > div > label:hover {
        background: linear-gradient(135deg, #16213e 0%, #1a1a2e 100%);
        border: 1px solid #FFE81F;
        transform: translateX(5px);
        box-shadow: 0 0 15px rgba(255, 232, 31, 0.3);
    }
    
    /* Dividers */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #FFE81F, transparent);
        margin: 1.5rem 0;
    }
    
    /* Status badges */
    .stSuccess, .stWarning, .stError {
        font-family: 'Rajdhani', sans-serif;
        font-weight: 600;
        border-radius: 8px;
        padding: 10px 16px;
        border: 1px solid;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, #1a3a1a 0%, #0f2f0f 100%);
        border-color: #4ade80;
        color: #4ade80 !important;
        box-shadow: 0 0 15px rgba(74, 222, 128, 0.2);
    }
    
    .stWarning {
        background: linear-gradient(135deg, #3a2a1a 0%, #2f1f0f 100%);
        border-color: #fbbf24;
        color: #fbbf24 !important;
        box-shadow: 0 0 15px rgba(251, 191, 36, 0.2);
    }
    
    .stError {
        background: linear-gradient(135deg, #3a1a1a 0%, #2f0f0f 100%);
        border-color: #ef4444;
        color: #ef4444 !important;
        box-shadow: 0 0 15px rgba(239, 68, 68, 0.2);
    }
    
    /* Markdown no sidebar */
    [data-testid="stSidebar"] .element-container p {
        color: #a8b2d1;
        font-size: 14px;
    }
    
    [data-testid="stSidebar"] strong {
        color: #FFE81F;
        font-weight: 600;
    }
    
    /* Links */
    a {
        color: #FFE81F !important;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    a:hover {
        color: #ffffff !important;
        text-shadow: 0 0 10px rgba(255, 232, 31, 0.8);
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    # LOGO / TÍTULO
    st.markdown(
        """
        <div style="text-align: center; padding: 1.5rem 0; margin-bottom: 1rem;">
            <h2 style="font-size: 28px; margin-bottom: 0.5rem; animation: pulse 2s ease-in-out infinite;">
                🌌 Star Wars Explorer
            </h2>
            <p style="font-size: 14px; color: #6b7280; font-family: 'Rajdhani', sans-serif; letter-spacing: 1px;">
                API + Streamlit
            </p>
        </div>
        <style>
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.8; }
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # NAVEGAÇÃO
    st.markdown("### 🧭 Navegação")

    page = st.radio(
        "Ir para:",
        [
            "🏠 Home",
            "🔎 Busca",
            "🎬 Filmes",
        ],
        label_visibility="collapsed"
    )

    st.divider()

    # SOBRE
    st.markdown("### ℹ️ Sobre")

    st.markdown(
        """
        <div style="padding: 1rem; background: rgba(255, 232, 31, 0.05); border-radius: 8px; border: 1px solid rgba(255, 232, 31, 0.2);">
            <p style="margin: 0; line-height: 1.8;">
                • Case Técnico<br>
                • Streamlit<br>
                • SWAPI
            </p>
            <p style="margin-top: 1rem; margin-bottom: 0;">
                Desenvolvido por<br>
                <strong style="font-size: 16px;">Emanuel Victor</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ----- ROTEAMENTO DE PÁGINAS -----

if page == "🏠 Home":
    from views.home import render
    render()

if page == "🎬 Filmes":
    from views.filmes import render
    render()

if page == "🔎 Busca":
    from views.busca import render
    render()