import os
import requests
import pandas as pd
from dotenv import load_dotenv
from IPython.display import display

# Carrega variáveis do .env
load_dotenv()

# Obtém credenciais da API
API_KEY = os.getenv("API_KEY")
TOKEN_API = os.getenv("TOKEN_API")

# URL da API do TMDB para filmes mais bem avaliados
BASE_URL = "https://api.themoviedb.org/3"
ENDPOINT = "/movie/top_rated"
PARAMS = {
    "api_key": API_KEY,
    "language": "pt-BR",
    "page": 1  # Obtendo apenas a primeira página de resultados
}

# Cabeçalhos para autenticação
HEADERS = {
    "Authorization": f"Bearer {TOKEN_API}",
    "Content-Type": "application/json;charset=utf-8"
}

# Fazendo requisição à API
response = requests.get(f"{BASE_URL}{ENDPOINT}", headers=HEADERS, params=PARAMS)

if response.status_code == 200:
    data = response.json()
    
    filmes = []
    for movie in data['results']:
        filme_info = {
            'Título': movie['title'],
            'Data de lançamento': movie['release_date'],
            'Visão geral': movie['overview'],
            'Votos': movie['vote_count'],
            'Média de votos': movie['vote_average']
        }
        filmes.append(filme_info)

    # Criando DataFrame com os filmes
    df = pd.DataFrame(filmes)

    # Exibir o DataFrame
    display(df)

else:
    print(f"Erro ao acessar a API: {response.status_code}")
    print(response.text)
