# Usar uma imagem base oficial do Python
FROM python:3.12-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instalar dependências necessárias
RUN pip install --no-cache-dir pandas matplotlib

# Copiar o script de análise para o contêiner
COPY job.py .

# Definir o ponto de entrada para executar o script de análise
ENTRYPOINT ["python", "job.py"]
