import os
import json
import requests
import logging
import boto3
from datetime import datetime

# Configuração do Logging (Lambda já envia para CloudWatch)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Variáveis de ambiente
TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
S3_BUCKET = os.environ.get('S3_BUCKET')  # Nome do bucket destino

if not TMDB_API_KEY:
    logging.error("TMDB_API_KEY não configurada nas variáveis de ambiente.")
if not S3_BUCKET:
    logging.error("S3_BUCKET não configurado nas variáveis de ambiente.")

# Constantes de configuração
GENRES = "27,9648"  # Horror e Mystery
S3_PREFIX = "Raw/TMDB/JSON"  # Camada RAW para TMDB em formato JSON

# Criação de uma Session para reuso de conexões (boa prática para economia de recursos)
session = requests.Session()
s3_client = boto3.client('s3')

def discover_filmes_por_ano(ano, page):
    """
    Realiza a requisição ao endpoint Discover do TMDB para um ano específico.
    """
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        'api_key': TMDB_API_KEY,
        'with_genres': GENRES,
        'primary_release_year': ano,
        'page': page,
        'sort_by': 'popularity.desc'
    }
    try:
        response = session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Erro ao buscar dados para o ano {ano} página {page}: {e}")
        return None

def salvar_registros_s3(lista_registros, ano, contador_arquivo):
    """
    Salva um chunk de registros (apenas os itens de filme, sem a estrutura de página)
    em um objeto JSON no S3, agrupando até 100 registros por arquivo.
    """
    hoje = datetime.utcnow()
    # Cria o nome do arquivo (pode incluir um identificador único se necessário)
    filename = f"tmdb_{ano}_{contador_arquivo:03d}.json"
    # Monta o path de armazenamento conforme padrão:
    # <S3_BUCKET>/Raw/TMDB/JSON/<ano>/<mês>/<dia>/<arquivo>
    s3_key = f"{S3_PREFIX}/{hoje.year:04d}/{hoje.month:02d}/{hoje.day:02d}/{filename}"
    
    conteudo = json.dumps(lista_registros, ensure_ascii=False, indent=2)
    
    # Verificar se o conteúdo excede 10 MB (boa prática para evitar custos elevados de transferência)
    if len(conteudo.encode('utf-8')) > 10 * 1024 * 1024:
        logging.warning(f"[ALERTA] O objeto {filename} excede 10 MB. Ajuste a forma de particionar.")
        return False

    try:
        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key=s3_key,
            Body=conteudo.encode('utf-8'),
            ContentType='application/json'
        )
        logging.info(f"Objeto salvo em s3://{S3_BUCKET}/{s3_key} com {len(lista_registros)} registros.")
        return True
    except Exception as e:
        logging.error(f"Erro ao salvar objeto {s3_key} no S3: {e}")
        return False

def processa_ano(ano):
    """
    Processa os dados para um ano específico, paginando a API do TMDB,
    agrupando registros em chunks de 100 e salvando cada chunk no S3.
    """
    page = 1
    acumulador_registros = []  # Armazena os registros individuais (flatten)
    contador_arquivo = 1

    while True:
        data = discover_filmes_por_ano(ano, page)
        if data is None or 'results' not in data:
            logging.error("Erro ou dados inválidos, encerrando loop.")
            break

        results = data['results']
        if not results:
            logging.info("Nenhum resultado encontrado na página, encerrando loop.")
            break

        # Acumula os registros individuais
        acumulador_registros.extend(results)
        logging.info(f"Ano {ano} - Página {page}: acumulado {len(acumulador_registros)} registros.")

        # Enquanto houver 100 ou mais registros acumulados, salva um arquivo no S3
        while len(acumulador_registros) >= 100:
            chunk = acumulador_registros[:100]
            salvar_registros_s3(chunk, ano, contador_arquivo)
            contador_arquivo += 1
            # Remove os registros que já foram salvos
            acumulador_registros = acumulador_registros[100:]

        # Se a página retornou menos de 20 registros, assumimos que é a última página
        if len(results) < 20:
            logging.info("Menos de 20 registros retornados, fim dos dados para este ano.")
            break

        page += 1

    # Se ainda houver registros no acumulador, salva mesmo que não complete 100
    if acumulador_registros:
        logging.info(f"Faltaram {len(acumulador_registros)} registros para completar 100, salvando mesmo assim.")
        salvar_registros_s3(acumulador_registros, ano, contador_arquivo)

def lambda_handler(event, context):
    """
    Handler principal para o AWS Lambda.
    Espera receber o ano a ser processado no evento, ex: { "year": 2020 }
    """
    # Valida o input do evento
    ano = event.get("year")
    if not ano:
        logging.error("Evento inválido. É necessário informar o parâmetro 'year'.")
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Parâmetro 'year' ausente no evento."})
        }

    try:
        ano = int(ano)
    except ValueError:
        logging.error("Ano informado é inválido.")
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "O parâmetro 'year' deve ser um número inteiro."})
        }

    # Processa o ano solicitado
    processa_ano(ano)
    logging.info("Processamento concluído.")

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Processamento do ano {ano} concluído com sucesso."})
    }

# Para testes locais (não utilizado na execução no Lambda)
if __name__ == "__main__":
    # Exemplo de teste local, informando o ano via input
    ano_str = input("Digite o ano que deseja processar (ex: 2020): ")
    try:
        ano = int(ano_str)
    except ValueError:
        logging.error("Ano inválido!")
        exit(1)

    processa_ano(ano)
    logging.info("Processamento concluído.")
