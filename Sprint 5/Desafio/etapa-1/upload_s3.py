import os
import boto3
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

# Obtém credenciais e configurações a partir do .env
chaves = ("AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "BUCKET_NAME", "REGIAO")
creds = {chave: os.getenv(chave) for chave in chaves}

if not all(creds.values()):
    raise ValueError("Erro: Algumas credenciais não foram carregadas corretamente. Verifique o arquivo .env.")

# Conexão com o AWS S3 usando credenciais temporárias
s3_client = boto3.client(
    "s3",
    aws_access_key_id=creds["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=creds["AWS_SECRET_ACCESS_KEY"],
    aws_session_token=creds["AWS_SESSION_TOKEN"],
    region_name=creds["REGIAO"],
)

# Define o caminho local e os arquivos CSV a serem enviados
LOCAL_PATH = "/volume"
arquivos = {
    "Movies": os.path.join(LOCAL_PATH, "movies.csv"),
    "Series": os.path.join(LOCAL_PATH, "series.csv"),
}

# Geração do caminho dinâmico baseado na data atual (formato: AAAA/MM/DD)
data_path = datetime.today().strftime("%Y/%m/%d")

def upload_arquivo(caminho_local, tipo):
    """
    Realiza o upload de um arquivo para o bucket S3 dentro da estrutura definida.
    """
    if not os.path.exists(caminho_local):
        print(f"Arquivo {caminho_local} não encontrado. Pulei esse upload.")
        return
    
    nome_arquivo = os.path.basename(caminho_local)
    s3_path = f"Raw/Local/CSV/{tipo}/{data_path}/{nome_arquivo}"
    
    try:
        s3_client.upload_file(caminho_local, creds["BUCKET_NAME"], s3_path)
        print(f"Upload concluído: {s3_path}")
    except Exception as e:
        print(f"Erro no upload de {nome_arquivo}: {e}")

# Itera sobre os arquivos e realiza o upload
for tipo, caminho in arquivos.items():
    upload_arquivo(caminho, tipo)
