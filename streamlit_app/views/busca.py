import streamlit as st
import requests

API_URL = "http://localhost:8080"


def render():
    st.title("🔎 Busca de Recursos")
    st.caption("Consuma a API Star Wars aplicando filtros e ordenação")

    # --- FILTROS ---
    with st.container():
        resource_type = st.selectbox(
            "🧩 Tipo de recurso",
            ["people", "films", "planets", "starships", "vehicles", "species"]
        )

        name = st.text_input(
            "🔤 Filtro por nome (opcional)",
            placeholder="Ex: Luke, Tatooine, Falcon..."
        )

        st.subheader("🔠 Ordem alfabética")

        order = st.radio(
            "Ordenar resultados",
            ["asc", "desc"],
            format_func=lambda x: "A → Z" if x == "asc" else "Z → A",
            horizontal=True
        )

    st.divider()

    # --- AÇÃO ---
    if st.button("🚀 Buscar", use_container_width=True):
        params = {
            "type": resource_type,
            "order": order
        }

        if name:
            params["name"] = name

        with st.spinner("Buscando na galáxia..."):
            try:
                response = requests.get(
                    f"{API_URL}/search",
                    params=params,
                    timeout=20
                )
            except Exception:
                st.error("❌ Não foi possível conectar à API")
                return

        # --- RESULTADO ---
        if response.status_code == 200:
            data = response.json()

            st.success(
                f"🔍 {data['count']} resultado(s) encontrados "
                f"(ordem {'A → Z' if order == 'asc' else 'Z → A'})"
            )

            if data["count"] == 0:
                st.info("Nenhum resultado encontrado com os filtros aplicados.")
                return

            for item in data["results"]:
                with st.expander(item.get("name") or item.get("title")):
                    st.json(item)

        else:
            try:
                error = response.json().get("error")
            except Exception:
                error = "Erro inesperado"

            st.error(f"❌ Erro ao consultar a API: {error}")
