🌌 Star Wars API – Cloud Functions (GCP)

Este projeto foi desenvolvido como parte de um case técnico, utilizando Python e Google Cloud Functions, com consumo da API pública SWAPI (Star Wars API).

A aplicação expõe endpoints REST que permitem:

Busca genérica por recursos do universo Star Wars

Consulta de informações relacionadas a filmes (personagens, planetas, naves, etc.)

O foco do projeto está em arquitetura limpa, separação de responsabilidades, testabilidade e boas práticas em ambiente cloud.

🚀 Tecnologias Utilizadas

Python 3.10

Google Cloud Functions

Functions Framework (execução local)

Google Cloud API Gateway / Apigee (camada de exposição)

Pytest + unittest.mock (testes automatizados)

SWAPI – https://swapi.dev

🏗️ Arquitetura da Solução

A solução foi projetada utilizando uma arquitetura em camadas, promovendo baixo acoplamento e alta coesão.

Visão Geral da Arquitetura
Usuário
   ↓
API Gateway / Apigee
   ↓
Cloud Functions (Flask / Functions Framework)
   ↓
Service Layer
   ↓
SWAPI Client
   ↓
SWAPI (API Externa)

📐 Separação de Responsabilidades
main.py

Entry point das Cloud Functions

Responsável apenas por:

Receber requisições HTTP

Validar parâmetros básicos

Delegar a lógica para a camada de serviços

app/services/

Contém a lógica de negócio

Implementa:

Filtros

Ordenação

Regras de relacionamento entre entidades

Totalmente desacoplada da infraestrutura

app/swapi_client.py

Cliente dedicado para comunicação com a SWAPI

Centraliza:

Requisições HTTP

Normalização de respostas

Tratamento de variações de payload da API externa

tests/

Testes unitários dos serviços

Uso de mock para evitar dependência de APIs externas

✅ Benefícios dessa Arquitetura

Facilidade de manutenção

Testes unitários isolados

Clareza no fluxo de dados

Pronta para escalar ou migrar para outras infraestruturas

Adequada para ambientes serverless

starwars-api/
│
├── main.py
├── app/
│   ├── __init__.py
│   ├── swapi_client.py
│   └── services/
│       ├── __init__.py
│       ├── search.py
│       └── film_relations.py
│
├── tests/
│   ├── test_search.py
│   └── test_film_relations.py
│
├── streamlit_app/
│   ├── search_ui.py
│   └── film_relations_ui.py
│
├── requirements.txt
└── README.md


🔗 Endpoints Disponíveis
🔍 1. Busca Genérica

Permite consultar recursos da API Star Wars com filtro opcional por nome e ordenação alfabética.

Endpoint

GET /search


Parâmetros

Parâmetro	Obrigatório	Descrição
type	Sim	people, films, planets, starships, vehicles, species
name	Não	Filtro por nome ou título
order	Não	asc (padrão) ou desc

Exemplo

GET /search?type=people&name=luke&order=asc

🎬 2. Relações de um Filme

Permite consultar informações relacionadas a um filme específico.

Endpoint

GET /film-relations

GET /film-relations?film=A New Hope&relation=characters

Com filtro:

GET /film-relations?film=A New Hope&relation=characters&name=luke

🔄 Fluxo de Execução

O usuário faz uma requisição HTTP

O API Gateway recebe e valida a chamada

A Cloud Function processa a requisição

A camada de serviços executa a lógica de negócio

O cliente SWAPI consulta a API externa

Os dados são filtrados, ordenados e normalizados

A resposta é retornada em JSON

🧪 Testes Automatizados

Os testes foram implementados utilizando pytest e unittest.mock, cobrindo:

Busca genérica sem filtro

Busca com filtro por nome

Ordenação alfabética

Consulta de relações de filmes

Validação de parâmetros inválidos

Executar os testes

pytest

▶️ Execução Local
1️⃣ Criar ambiente virtual
python -m venv venv
source venv/bin/activate
# Windows: venv\Scripts\activate

2️⃣ Instalar dependências
pip install -r requirements.txt

3️⃣ Executar localmente
functions-framework --source main.py --target search --port 8080


Ou:

functions-framework --source main.py --target film_relations --port 8080

🔐 Autenticação e Segurança
Produção (GCP)

Em produção, a autenticação é delegada ao Google Cloud API Gateway / Apigee, responsável por:

Autenticação via API Key

Rate limiting

Logs e monitoramento

Controle de permissões

A Cloud Function permanece stateless e sem lógica de autenticação embutida, seguindo boas práticas de arquitetura cloud-native.

☁️ Deploy no Google Cloud

Cada função pode ser implantada separadamente:

gcloud functions deploy search \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated

gcloud functions deploy film_relations \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated


O API Gateway pode ser configurado para centralizar os endpoints e aplicar políticas de segurança.

🖥️ Interface de Demonstração (Streamlit)

Foi desenvolvida uma interface em Streamlit com o objetivo de:

Demonstrar o funcionamento da API

Facilitar a visualização dos dados

Apoiar a apresentação do case técnico

Funcionalidades da UI

Seleção de tipo de recurso

Filtro opcional por nome

Ordenação alfabética (A → Z / Z → A)

Consulta de relações entre filmes

Visualização estruturada dos resultados

Executar o Streamlit
streamlit run streamlit_app/search_ui.py


⚠️ O Streamlit não faz parte da arquitetura de produção, sendo utilizado apenas como camada de visualização para demonstração do projeto. 

📌 Considerações Finais

Este projeto demonstra:

Uso de Cloud Functions no GCP

Consumo de APIs externas

Arquitetura em camadas

Código limpo e testável

Boas práticas de backend e cloud

👤 Autor

Emanuel Victor
Desenvolvedor Backend
Python • Cloud • APIs • Arquitetura