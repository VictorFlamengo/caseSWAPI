import streamlit as st
import requests

API_URL = "http://localhost:8080/search"


def render():
    st.set_page_config(
        page_title="Star Wars API – Case Técnico",
        layout="centered"
    )

    # CSS customizado para a página de busca
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
        .stSelectbox > label, .stTextInput > label, .stRadio > label {
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
        
        /* Radio buttons */
        .stRadio > div {
            background: linear-gradient(135deg, rgba(26, 26, 46, 0.5) 0%, rgba(22, 33, 62, 0.5) 100%);
            border-radius: 10px;
            padding: 10px;
            border: 2px solid rgba(255, 232, 31, 0.2);
        }
        
        .stRadio > div > label {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            border-radius: 8px;
            padding: 10px 20px !important;
            margin: 5px !important;
            border: 2px solid transparent;
            transition: all 0.3s ease;
            font-family: 'Rajdhani', sans-serif;
            font-weight: 500;
            color: #a8b2d1 !important;
        }
        
        .stRadio > div > label:hover {
            border-color: #FFE81F;
            box-shadow: 0 0 15px rgba(255, 232, 31, 0.3);
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
        
        /* Results styling */
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
        
        /* Container styling */
        [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            border-radius: 12px;
            padding: 1.5rem;
            border: 2px solid rgba(255, 232, 31, 0.2);
            margin-bottom: 1rem;
            transition: all 0.3s ease;
        }
        
        [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"]:hover {
            border-color: #FFE81F;
            box-shadow: 0 4px 20px rgba(255, 232, 31, 0.2);
        }
        
        /* JSON viewer */
        .stJson {
            background: #0a0a1a !important;
            border-radius: 8px;
            border: 1px solid rgba(255, 232, 31, 0.2);
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
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="page-title">🌌 Star Wars API – Case Técnico</h1>', unsafe_allow_html=True)
    st.markdown(
        """
        <p class="page-subtitle">
            Interface criada para demonstrar o consumo da API desenvolvida no desafio técnico.<br><br>
            O endpoint permite <strong>consulta de recursos do universo Star Wars</strong>,  
            com <strong>filtro opcional por nome</strong> e <strong>ordenação alfabética</strong>.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # 🔧 FILTROS
    st.subheader("🔧 Parâmetros da busca")

    with st.form("search_form"):
        resource_type = st.selectbox(
            "🧩 Tipo de recurso",
            ["people", "films", "planets", "starships", "vehicles", "species"]
        )

        name = st.text_input(
            "🔎 Filtro por nome (opcional)",
            placeholder="Ex: Luke, Tatooine, Falcon"
        )

        order = st.radio(
            "🔠 Ordenação alfabética",
            ["asc", "desc"],
            format_func=lambda x: "A → Z" if x == "asc" else "Z → A",
            horizontal=True
        )

        submit = st.form_submit_button("🚀 Executar consulta")

    if not submit:
        return

    # 📡 REQUEST
    params = {
        "type": resource_type,
        "order": order
    }

    if name:
        params["name"] = name

    with st.spinner("🔄 Consultando a API..."):
        try:
            response = requests.get(
                API_URL,
                params=params,
                timeout=20
            )
        except Exception:
            st.error("❌ Não foi possível estabelecer conexão com a API")
            return

    st.divider()

    # 📊 RESULTADO
    if response.status_code != 200:
        try:
            error = response.json().get("error")
        except Exception:
            error = "Erro inesperado"

        st.error(f"❌ Erro ao consultar a API: {error}")
        return

    data = response.json()

    st.subheader("📊 Resultado da consulta")

    st.markdown(
        f"""
        <div class="result-header">
            <p class="result-stat"><strong>Recurso:</strong> <code>{resource_type}</code></p>
            <p class="result-stat"><strong>Ordenação:</strong> {'A → Z' if order == 'asc' else 'Z → A'}</p>
            <p class="result-stat"><strong>Total encontrado:</strong> {data['count']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if data["count"] == 0:
        st.info("ℹ️ Nenhum resultado encontrado com os filtros informados.")
        return

    # 🧩 LISTAGEM
    for item in data["results"]:
        title = item.get("name") or item.get("title")

        with st.container(border=True):
            st.markdown(f"### ⭐ {title}")
            st.json(item)