# Usa uma imagem base do Python leve
FROM python:3.12-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos do projeto para dentro do contêiner
COPY requirements.txt /app/
COPY upload_s3.py /app/

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Define um volume onde os arquivos CSV ficarão armazenados
VOLUME ["/volume"]

# Define o ponto de entrada para executar o script automaticamente
ENTRYPOINT ["python", "/app/upload_s3.py"]