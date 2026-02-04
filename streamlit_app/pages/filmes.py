import streamlit as st
import requests

API_URL = "http://localhost:8080"

filmes = [
    "A New Hope",
    "The Empire Strikes Back",
    "Return of the Jedi",
    "The Phantom Menace",
    "Attack of the Clones",
    "Revenge of the Sith"
]

def render():
    st.title("🎬 Relações entre Filmes")

    film = st.selectbox("Nome do filme", filmes)       
    relation = st.selectbox(
        "Tipo de relação",
        ["characters", "planets", "starships", "vehicles", "species"]
    )

    if st.button("Buscar relações"):
        if not film:
            st.warning("Informe o nome do filme")
        else:
            params = {"film": film, "relation": relation}

            with st.spinner("Consultando o hiper-espaço..."):
                response = requests.get(API_URL, params=params)

            if response.status_code == 200:
                st.json(response.json())
            else:
                st.error("Erro ao buscar relações")
