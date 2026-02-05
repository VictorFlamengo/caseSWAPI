import streamlit as st
import requests

API_URL = "http://localhost:8080/film-relations"

FILMES = [
    "A New Hope",
    "The Empire Strikes Back",
    "Return of the Jedi",
    "The Phantom Menace",
    "Attack of the Clones",
    "Revenge of the Sith"
]

RELATIONS = {
    "characters": "Personagens",
    "planets": "Planetas",
    "starships": "Naves",
    "vehicles": "Veículos",
    "species": "Espécies"
}

def render():
    st.set_page_config(
        page_title="Star Wars API – Case Técnico",
        layout="centered"
    )

    # CSS customizado para a página de filmes
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&family=Audiowide&display=swap');
        
        /* Page title */
        .page-title {
            font-family: 'Audiowide', cursive;
            font-size: 3rem;
            text-align: center;
            background: linear-gradient(135deg, #FFE81F 0%, #ffffff 50%, #FFE81F 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
        }
        
        .page-subtitle {
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.1rem;
            color: #a8b2d1;
            text-align: center;
            line-height: 1.8;
        }
        
        /* Form styling */
        .stSelectbox > label, .stTextInput > label {
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 1rem !important;
            font-weight: 600 !important;
            color: #FFE81F !important;
            letter-spacing: 0.5px;
        }
        
        .stSelectbox > div > div, .stTextInput > div > div > input {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%) !important;
            border: 2px solid rgba(255, 232, 31, 0.3) !important;
            border-radius: 8px !important;
            color: #a8b2d1 !important;
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 1rem !important;
            transition: all 0.3s ease;
        }
        
        .stSelectbox > div > div:hover, .stTextInput > div > div > input:hover {
            border-color: #FFE81F !important;
            box-shadow: 0 0 15px rgba(255, 232, 31, 0.3) !important;
        }
        
        .stSelectbox > div > div:focus-within, .stTextInput > div > div > input:focus {
            border-color: #FFE81F !important;
            box-shadow: 0 0 20px rgba(255, 232, 31, 0.5) !important;
        }
        
        /* Submit button */
        .stButton > button {
            width: 100%;
            background: linear-gradient(135deg, #FFE81F 0%, #ffd700 100%) !important;
            color: #000000 !important;
            font-family: 'Audiowide', cursive !important;
            font-size: 1.1rem !important;
            font-weight: 700 !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.8rem 2rem !important;
            letter-spacing: 2px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 20px rgba(255, 232, 31, 0.4);
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 30px rgba(255, 232, 31, 0.6);
            filter: brightness(1.1);
        }
        
        /* Results header */
        .result-header {
            background: linear-gradient(135deg, rgba(26, 26, 46, 0.8) 0%, rgba(22, 33, 62, 0.8) 100%);
            border-radius: 12px;
            padding: 1.5rem;
            border: 2px solid rgba(255, 232, 31, 0.3);
            margin-bottom: 1.5rem;
        }
        
        .result-stat {
            font-family: 'Rajdhani', sans-serif;
            color: #a8b2d1;
            font-size: 1.1rem;
            line-height: 1.8;
        }
        
        .result-stat strong {
            color: #FFE81F;
        }
        
        /* Result items */
        [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            border-radius: 12px;
            padding: 1.2rem;
            border: 2px solid rgba(255, 232, 31, 0.2);
            margin-bottom: 1rem;
            transition: all 0.3s ease;
        }
        
        [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"]:hover {
            border-color: #FFE81F;
            transform: translateX(5px);
            box-shadow: 0 4px 20px rgba(255, 232, 31, 0.3);
        }
        
        /* Item title */
        [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] p:first-child strong {
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.3rem;
            color: #FFE81F;
            font-weight: 700;
        }
        
        /* Caption (URL) */
        .stCaption {
            font-family: 'Rajdhani', sans-serif;
            color: #6b7280 !important;
            font-size: 0.9rem;
            font-family: monospace;
        }
        
        /* Alerts */
        .stAlert {
            font-family: 'Rajdhani', sans-serif;
            font-weight: 600;
            border-radius: 10px;
            border-width: 2px;
        }
        
        /* Spinner */
        .stSpinner > div {
            border-top-color: #FFE81F !important;
        }
        
        /* Section headers */
        h3 {
            font-family: 'Audiowide', cursive !important;
            color: #FFE81F !important;
            font-size: 1.8rem !important;
            letter-spacing: 1px;
        }
        
        /* Columns spacing */
        [data-testid="column"] {
            padding: 0 0.5rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="page-title">🌌 Star Wars API – Case Técnico</h1>', unsafe_allow_html=True)
    st.markdown(
        """
        <p class="page-subtitle">
            Esta interface demonstra o consumo da API desenvolvida para o desafio técnico.<br><br>
            É possível consultar <strong>relações entre filmes e recursos do universo Star Wars</strong>,  
            com suporte a <strong>filtro opcional por nome</strong>.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # 🔧 Filtros
    st.subheader("🔧 Parâmetros da consulta")

    with st.form("film_relations_form"):
        col1, col2 = st.columns(2)

        with col1:
            film = st.selectbox("🎬 Filme", FILMES)

        with col2:
            relation = st.selectbox(
                "🔗 Tipo de relação",
                options=list(RELATIONS.keys()),
                format_func=lambda r: RELATIONS[r]
            )

        name_filter = st.text_input(
            "🔎 Filtro por nome (opcional)",
            placeholder="Ex: Luke, Tatooine, Falcon"
        )

        submit = st.form_submit_button("🚀 Executar consulta")

    if not submit:
        return

    # 📡 Request
    params = {
        "film": film,
        "relation": relation
    }

    if name_filter:
        params["name"] = name_filter

    with st.spinner("🔄 Consultando a API..."):
        response = requests.get(API_URL, params=params)

    if response.status_code != 200:
        st.error("❌ Erro ao consultar a API")
        return

    data = response.json()

    st.divider()

    # 📊 Resultado
    st.subheader("📊 Resultado da consulta")

    st.markdown(
        f"""
        <div class="result-header">
            <p class="result-stat"><strong>Filme:</strong> {data['film']}</p>
            <p class="result-stat"><strong>Relação:</strong> {RELATIONS[data['relation']]}</p>
            <p class="result-stat"><strong>Total encontrado:</strong> {data['count']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if data["count"] == 0:
        st.info("ℹ️ Nenhum resultado encontrado com os filtros informados.")
        return

    # 🧩 Lista de resultados
    for item in data["results"]:
        with st.container(border=True):
            st.markdown(f"**⭐ {item['name']}**")
            st.caption(item["url"])