import streamlit as st

with st.sidebar:
    # LOGO / TÍTULO
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 24px;">🌌 Star Wars Explorer</h2>
        <p style="text-align: center; font-size: 14px; color: gray;">
            API + Streamlit
        </p>
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
            "📄 Documentação"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    # STATUS DA API
    st.markdown("### ⚙️ Status da API")

    API_URL = "http://localhost:8080"

    try:
        import requests
        response = requests.get(f"{API_URL}/health", timeout=2)

        if response.status_code == 200:
            st.success("API Online")
        else:
            st.warning("⚠️ API está inativa")

    except Exception:
        st.error("API Offline")

    st.divider()

    # SOBRE
    st.markdown("### ℹ️ Sobre")

    st.markdown(
        """
        - Case Técnico  
        - Streamlit  
        - SWAPI  

        Desenvolvido por  
        **Emanuel Victor**
        """
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
