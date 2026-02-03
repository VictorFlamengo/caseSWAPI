Star Wars API – Cloud Functions (GCP)

Este projeto foi desenvolvido como parte de um case técnico, utilizando Google Cloud Platform (GCP), Python e Cloud Functions, consumindo dados da API pública SWAPI (Star Wars API).

A aplicação expõe endpoints que permitem consultar dados do universo Star Wars, incluindo buscas genéricas e informações correlacionadas, como personagens, planetas e naves de um filme específico.

🚀 Tecnologias Utilizadas

Python 3.10

Google Cloud Functions

Functions Framework (execução local)

API Gateway / Apigee (camada de exposição da API)

Pytest (testes automatizados)

SWAPI (https://swapi.dev)

🏗️ Arquitetura da Solução

A aplicação segue uma separação clara de responsabilidades:

main.py
Entry point das Cloud Functions (infraestrutura)

app/
Contém toda a lógica de negócio da aplicação

services/ → regras e processamento dos dados

swapi_client.py → comunicação com a SWAPI

tests/
Testes unitários dos serviços

Essa estrutura facilita:

manutenção

testes

deploy no GCP

desacoplamento da infraestrutura

📁 Estrutura do Projeto
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
├── requirements.txt
└── README.md

🔗 Endpoints Disponíveis
🔍 1. Busca Genérica

Permite consultar recursos da API do Star Wars com filtro opcional por nome.

Endpoint:

GET /search


Parâmetros:

type (obrigatório): people, films, planets, starships, vehicles, species

name (opcional): filtro por nome ou título

Exemplo:

GET /search?type=people&name=luke

🎬 2. Informações Relacionadas a um Filme

Permite consultar dados relacionados a um filme específico, como personagens, planetas, naves, veículos ou espécies.

Endpoint:

GET /film-relations


Parâmetros:

film (obrigatório): nome do filme

relation (obrigatório):

characters

planets

starships

vehicles

species

Exemplo:

GET /film-relations?film=A New Hope&relation=characters

🧪 Testes Automatizados

Os testes foram implementados utilizando pytest e unittest.mock, cobrindo:

Busca genérica sem filtro

Busca com filtro por nome

Consulta de relações de filmes

Validação de parâmetros inválidos

Executar os testes:
pytest

▶️ Executando Localmente
1. Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

2. Instalar dependências
pip install -r requirements.txt

3. Rodar função localmente
functions-framework --source main.py --target search --port 8080


Ou:

functions-framework --source main.py --target film_relations --port 8080

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


O API Gateway / Apigee pode ser utilizado para centralizar os endpoints e aplicar políticas como autenticação, rate limit e monitoramento.

📌 Considerações Finais

Este projeto demonstra:

uso de Cloud Functions no GCP

consumo de APIs externas

organização de código

testes automatizados

boas práticas de arquitetura

👤 Autor

Emanuel Victor