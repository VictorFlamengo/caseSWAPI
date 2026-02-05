import streamlit as st

def render():

    st.set_page_config(
        page_title="Star Wars Explorer",
        layout="wide"
    )

    # CSS adicional para a página home
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&family=Audiowide&display=swap');
        
        /* Hero section */
        .hero-title {
            font-family: 'Audiowide', cursive;
            font-size: 4rem;
            text-align: center;
            background: linear-gradient(135deg, #FFE81F 0%, #ffffff 50%, #FFE81F 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 0 40px rgba(255, 232, 31, 0.5);
            margin-bottom: 1rem;
            animation: shine 3s ease-in-out infinite;
        }
        
        @keyframes shine {
            0%, 100% { filter: brightness(1); }
            50% { filter: brightness(1.3); }
        }
        
        .hero-subtitle {
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.3rem;
            text-align: center;
            color: #a8b2d1;
            letter-spacing: 1px;
            line-height: 1.6;
        }
        
        /* Feature cards */
        .feature-card {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            border-radius: 15px;
            padding: 2rem;
            border: 2px solid rgba(255, 232, 31, 0.2);
            transition: all 0.4s ease;
            height: 100%;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        }
        
        .feature-card:hover {
            border-color: #FFE81F;
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(255, 232, 31, 0.3);
        }
        
        .feature-icon {
            font-size: 3rem;
            text-align: center;
            margin-bottom: 1rem;
            filter: drop-shadow(0 0 10px rgba(255, 232, 31, 0.5));
        }
        
        .feature-title {
            font-family: 'Audiowide', cursive;
            font-size: 1.5rem;
            color: #FFE81F;
            text-align: center;
            margin-bottom: 1rem;
            letter-spacing: 1px;
        }
        
        .feature-text {
            font-family: 'Rajdhani', sans-serif;
            color: #a8b2d1;
            text-align: center;
            font-size: 1.1rem;
            line-height: 1.6;
        }
        
        /* Section styling */
        .section-title {
            font-family: 'Audiowide', cursive;
            font-size: 2.5rem;
            color: #FFE81F;
            text-shadow: 0 0 20px rgba(255, 232, 31, 0.6);
            margin-bottom: 1.5rem;
            letter-spacing: 2px;
        }
        
        .content-box {
            background: linear-gradient(135deg, rgba(26, 26, 46, 0.6) 0%, rgba(22, 33, 62, 0.6) 100%);
            border-radius: 12px;
            padding: 2rem;
            border: 1px solid rgba(255, 232, 31, 0.2);
            margin: 1.5rem 0;
        }
        
        .content-text {
            font-family: 'Rajdhani', sans-serif;
            color: #a8b2d1;
            font-size: 1.1rem;
            line-height: 1.8;
        }
        
        /* Steps list */
        .steps-list {
            font-family: 'Rajdhani', sans-serif;
            color: #a8b2d1;
            font-size: 1.1rem;
            line-height: 2;
        }
        
        .steps-list strong {
            color: #FFE81F;
        }
        
        /* Footer */
        .footer-text {
            font-family: 'Rajdhani', sans-serif;
            text-align: center;
            font-size: 1rem;
            color: #6b7280;
            letter-spacing: 1px;
            padding: 2rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

    # HERO
    st.markdown(
        """
        <div style="padding: 3rem 0;">
            <h1 class="hero-title">🌌 Star Wars Explorer</h1>
            <p class="hero-subtitle">
                Explore dados do universo Star Wars consumindo a API SWAPI<br>
                através de uma API própria, documentada e organizada.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # SEÇÃO PRINCIPAL - Feature Cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🔎</div>
                <h3 class="feature-title">Busca Inteligente</h3>
                <p class="feature-text">
                    Pesquise personagens, planetas, naves e espécies  
                    utilizando filtros dinâmicos consumindo a API.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🎬</div>
                <h3 class="feature-title">Relações de Filmes</h3>
                <p class="feature-text">
                    Veja quais personagens, planetas e naves  
                    aparecem em cada filme da saga.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🔐</div>
                <h3 class="feature-title">API Profissional</h3>
                <p class="feature-text">
                    API com autenticação, logs, rate limit  
                    e boas práticas de backend em Python.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # SOBRE O PROJETO
    st.markdown('<h2 class="section-title">📌 Sobre o Projeto</h2>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="content-box">
            <p class="content-text">
                Este projeto foi desenvolvido como <strong>case técnico</strong> com o objetivo de demonstrar:
            </p>
            <ul class="content-text" style="margin-top: 1rem;">
                <li>Consumo de API externa (SWAPI)</li>
                <li>Criação de uma API intermediária em Python</li>
                <li>Organização de código</li>
                <li>Logs, autenticação e rate limiting</li>
                <li>Frontend simples com Streamlit</li>
            </ul>
            <p class="content-text" style="margin-top: 1rem;">
                A aplicação Streamlit atua como <strong>cliente da API</strong>, permitindo controlar
                parâmetros, filtros e tipos de recursos de forma visual.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # COMO USAR
    st.markdown('<h2 class="section-title">🚀 Como utilizar</h2>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="content-box">
            <div class="steps-list">
                1. Use o menu lateral para navegar<br>
                2. Acesse a página de <strong>Busca</strong> para consultar recursos<br>
                3. Explore <strong>Filmes</strong> para ver relações entre entidades<br>
                4. Todas as informações vêm da API local (<code>localhost</code>)
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # FOOTER
    st.markdown(
        """
        <p class="footer-text">
            Desenvolvido por <strong style="color: #FFE81F;">Emanuel Victor</strong> • Case Técnico • Python + Streamlit
        </p>
        """,
        unsafe_allow_html=True
    )