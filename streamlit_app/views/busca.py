import streamlit as st
import requests

API_URL = "http://localhost:8080/search"


def render():
    st.set_page_config(
        page_title="Star Wars API – Case Técnico",
        layout="centered"
    )

    st.title("🌌 Star Wars API – Case Técnico")
    st.markdown(
        """
        Interface criada para demonstrar o consumo da API desenvolvida no desafio técnico.

        O endpoint permite **consulta de recursos do universo Star Wars**,  
        com **filtro opcional por nome** e **ordenação alfabética**.
        """
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

        submit = st.form_submit_button("Executar consulta")

    if not submit:
        return

    # 📡 REQUEST
    params = {
        "type": resource_type,
        "order": order
    }

    if name:
        params["name"] = name

    with st.spinner("Consultando a API..."):
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
        **Recurso:** `{resource_type}`  
        **Ordenação:** {'A → Z' if order == 'asc' else 'Z → A'}  
        **Total encontrado:** {data['count']}
        """
    )

    if data["count"] == 0:
        st.info("Nenhum resultado encontrado com os filtros informados.")
        return

    # 🧩 LISTAGEM
    for item in data["results"]:
        title = item.get("name") or item.get("title")

        with st.container(border=True):
            st.markdown(f"### {title}")
            st.json(item)
