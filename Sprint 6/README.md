## Estrutura de Pastas
A pasta **Sprint 6** está organizada da seguinte forma:

```
Sprint 6/
├─ Certificados/  # Certificados conquistados durante a sprint, Obtivemos certificados da AWS nessa sprint
├─ Desafio/       # Implementações relacionadas ao desafio da sprint
├─ Evidencias/    # Imagens que comprovam a execução das atividades do desafio
├─ Exercicios/    # Scripts e resoluções dos exercícios
└─ README.md      # Documentação da Sprint 6
```

---

## Certificados

Os certificados obtidos durante a Sprint 6 estão disponíveis na pasta [Certificados](Certificados/). Obtivemos certificados da AWS nesta sprint.

---
### Desafio

A pasta **Desafio** contém todos os artefatos relacionados ao desafio desta sprint. A estrutura está organizada para facilitar o entendimento das entregas e inclui os seguintes itens:

- **job-csv.py/**: Realiza o processamento e a transformação dos arquivos CSV contendo os dados de filmes e séries para a camada Trusted.
- **job-json.py/**: Realiza o processamento e a transformação dos arquivos JSON do TMDB para a camada Trusted.
- **Arquivo README.md**: Documentação detalhada sobre o desafio, incluindo as etapas e os resultados obtidos.

---

## Evidências

As evidências para validação das execuções realizadas estão armazenadas na pasta [Evidencias](Evidencias/). Esta pasta contém capturas de tela e outros registros que comprovam a execução das atividades da sprint.

Exemplo de evidência gerada:

![log](./Evidencias/log-job.png)

---

## [Exercicios](Exercicios/)

Os exercícios foram organizados seguindo a estrutura do PB.

### Parte 1: Geração e massa de dados

- Etapa 1 – Números Aleatórios Invertidos

```python
import random

numeros = []
for _ in range(250):
    numeros.append(random.randint(1, 1000))

numeros.reverse()
print(numeros)
```

---

## Parte 2 – Análise com Apache Spark

- Etapa 1 - Inicialmente, prepararemos o ambiente, definindo o diretório onde nosso código será desenvolvido. 
- Para este diretório, copiaremos o arquivo `nomes_aleatorios.txt`.

Em nosso script Python, importaremos as bibliotecas necessárias:

```python
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

# Inicializando SparkSession com suporte a SQL
spark = SparkSession     .builder     .master('local[*]')     .appName('Exercicio Intro')     .getOrCreate()

# Carregando o arquivo nomes_aleatorios.txt como CSV (cada linha é uma entrada)
df_nomes = spark.read.csv('nomes_aleatorios.txt', header=False, inferSchema=True)

# Exibindo as 5 primeiras linhas do DataFrame
df_nomes.show(5)

# Finalizando a sessão Spark após o uso
spark.stop()
```

