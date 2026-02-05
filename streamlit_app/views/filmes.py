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

    st.title("🌌 Star Wars API – Case Técnico")
    st.markdown(
        """
        Esta interface demonstra o consumo da API desenvolvida para o desafio técnico.
        
        É possível consultar **relações entre filmes e recursos do universo Star Wars**,  
        com suporte a **filtro opcional por nome**.
        """
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

        submit = st.form_submit_button("Executar consulta")

    if not submit:
        return

    # 📡 Request
    params = {
        "film": film,
        "relation": relation
    }

    if name_filter:
        params["name"] = name_filter

    with st.spinner("Consultando a API..."):
        response = requests.get(API_URL, params=params)

    if response.status_code != 200:
        st.error("Erro ao consultar a API")
        return

    data = response.json()

    st.divider()

    # 📊 Resultado
    st.subheader("📊 Resultado da consulta")

    st.markdown(
        f"""
        **Filme:** {data['film']}  
        **Relação:** {RELATIONS[data['relation']]}  
        **Total encontrado:** {data['count']}
        """
    )

    if data["count"] == 0:
        st.info("Nenhum resultado encontrado com os filtros informados.")
        return

    # 🧩 Lista de resultados
    for item in data["results"]:
        with st.container(border=True):
            st.markdown(f"**{item['name']}**")
            st.caption(item["url"])
