# Usar uma imagem base oficial do Python
FROM python:3.12-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instalar dependências necessárias
RUN pip install --no-cache-dir pandas

# Copiar o script ETL para o contêiner
COPY etl.py /app/

# Configurar o volume para persistência de dados
VOLUME ["/volume"]

# Definir o ponto de entrada para executar o script ETL
ENTRYPOINT ["python", "etl.py"]
