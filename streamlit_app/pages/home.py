import streamlit as st

def render():

    st.set_page_config(
        page_title="Star Wars Explorer",
        layout="wide"
    )

    # HERO
    st.markdown(
        """
        <h1 style="text-align: center;">🌌 Star Wars Explorer</h1>
        <p style="text-align: center; font-size: 18px;">
            Explore dados do universo Star Wars consumindo a API SWAPI
            através de uma API própria, documentada e organizada.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # SEÇÃO PRINCIPAL
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🔎 Busca Inteligente")
        st.write(
            """
            Pesquise personagens, planetas, naves e espécies  
            utilizando filtros dinâmicos consumindo a API.
            """
        )

    with col2:
        st.markdown("### 🎬 Relações de Filmes")
        st.write(
            """
            Veja quais personagens, planetas e naves  
            aparecem em cada filme da saga.
            """
        )

    with col3:
        st.markdown("### 🔐 API Profissional")
        st.write(
            """
            API com autenticação, logs, rate limit  
            e boas práticas de backend em Python.
            """
        )

    st.divider()

    # SOBRE O PROJETO
    st.markdown("## 📌 Sobre o Projeto")

    st.write(
        """
    Este projeto foi desenvolvido como **case técnico** com o objetivo de demonstrar:

    - Consumo de API externa (SWAPI)
    - Criação de uma API intermediária em Python
    - Organização de código
    - Logs, autenticação e rate limiting
    - Frontend simples com Streamlit

    A aplicação Streamlit atua como **cliente da API**, permitindo controlar
    parâmetros, filtros e tipos de recursos de forma visual.
    """
    )

    st.divider()

    # COMO USAR
    st.markdown("## 🚀 Como utilizar")

    st.markdown(
        """
    1. Use o menu lateral para navegar  
    2. Acesse a página de **Busca** para consultar recursos  
    3. Explore **Filmes** para ver relações entre entidades  
    4. Todas as informações vêm da API local (`localhost`)
    """
    )

    st.divider()

    # FOOTER
    st.markdown(
        """
        <p style="text-align: center; font-size: 14px; color: gray;">
            Desenvolvido por Emanuel Victor • Case Técnico • Python + Streamlit
        </p>
        """,
        unsafe_allow_html=True
    )

