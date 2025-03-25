# Desafio: Criação da Camada Refined no AWS Glue

## 1. Descrição do Desafio
Este desafio consiste em criar um **job do AWS Glue** que leia dados da camada Trusted (armazenados em formato Parquet/CSV no S3), aplique transformações e gere tabelas na camada **Refined**. O objetivo é organizar os dados em um modelo dimensional, facilitando consultas e análises posteriores, por exemplo, no Amazon Athena.

## Anagrama do modelo dimensional:
![anagrama](../Evidencias/anagrama.png)


## 2. Tecnologias Utilizadas
- **AWS Glue** para orquestração e execução do job.
- **PySpark** (dentro do Glue) para leitura, transformação e gravação dos dados.
- **Amazon S3** como data lake para armazenar os arquivos Trusted e Refined.
- **Amazon Athena** (opcional) para consultas e validações.

## 3. Arquitetura e Modelo de Dados
A arquitetura segue o fluxo:
1. **Trusted**: Armazena dados após processos de limpeza básicos.
2. **Refined**: Recebe dados prontos para análise, organizados em Fatos e Dimensões.

### Modelo de Dados da Camada Refined
O modelo é composto pelas seguintes tabelas:

1. **fato_series**  
   - `id_tmdb` (bigint)  
   - `nota_media` (double)  
   - `votos_totais` (bigint)  
   - `popularidade` (double)  
   - `data_lancamento` (string)  
   - `temporada` (int)  
   - `episodio` (int)

2. **dim_serie**  
   - `id_tmdb` (bigint)  
   - `id_csv` (string)  
   - `nome` (string)  
   - `genero` (string)  
   - `idioma_original` (string)  
   - `pais_origem` (string)  
   - `ano_lancamento` (string)  
   - `status` (string)

3. **dim_elenco**  
   - `elenco_id` (bigint)  
   - `id_tmdb` (bigint)  
   - `nome_ator` (string)  
   - `popularidade_ator` (double)  
   - `personagem` (string)  
   - `ordem` (bigint)

4. **dim_tempo**  
   - `data_completa` (string)  
   - `ano` (int)  
   - `mes` (int)  
   - `dia` (int)

5. **dim_sentimento**  
   - `id_tmdb` (bigint)  
   - `texto_overview` (string)

Essas tabelas são salvas em formato **Parquet** na camada Refined.

## 4. Passo a Passo do Job
Abaixo, um resumo das etapas do arquivo `refined_job.py`:

1. **Captura dos Parâmetros e Inicialização**  
   - Recebe o nome do job via `getResolvedOptions`.
   - Inicializa o SparkContext e o GlueContext.

2. **Definição dos Caminhos S3**  
   - `TRUSTED_PATH` aponta para a localização dos dados Trusted.  
   - `REFINED_PATH` aponta para a localização dos dados Refined.

3. **Leitura dos Dados**  
   - Lê tabelas Parquet/CSV da camada Trusted (`df_reviews`, `df_detalhes`, `df_csv`, etc.).

4. **Criação das Tabelas**  
   - **Fato (fato_series)**: Seleciona campos relevantes (nota média, votos, data de lançamento, etc.).  
   - **Dimensão Série (dim_serie)**: Une dados de diferentes fontes (JSON e CSV), criando colunas com chaves separadas (`id_tmdb` e `id_csv`).  
   - **Dimensão Elenco (dim_elenco)**: Explode o campo de créditos para obter detalhes do elenco (atores, popularidade, personagens).  
   - **Dimensão Tempo (dim_tempo)**: Extrai ano, mês e dia a partir da data de lançamento.  
   - **Dimensão Sentimento (dim_sentimento)**: Armazena o overview (texto) para análises textuais.

5. **Escrita na Camada Refined**  
   - Escreve cada DataFrame em formato Parquet no S3, usando `mode("overwrite")`.

6. **Finalização**  
   - Exibe mensagens de conclusão e chama `job.commit()`.

## 5. Evidências e Prints

### 5.1. Execução do Job no AWS Glue

![log](../Evidencias/log.png)

### 5.2. Estrutura no S3

![s3](../Evidencias/s3.png)

### 5.3. Consultas no Athena

A consulta a seguir foi desenvolvida para validar a consistência do nosso modelo dimensional. Ela integra as principais tabelas do modelo (fato e dimensões) e permite verificar se os dados foram carregados corretamente e se os relacionamentos estão funcionando conforme esperado.

## O que a consulta faz:

- **Join entre Fato e Dimensão de Séries (dim_serie):**  
  A união é realizada pelo campo `id_tmdb`. Essa junção garante que os detalhes da série (como nome, gênero, idioma, país de origem, ano de lançamento e status) estejam associados corretamente aos indicadores de desempenho (nota média, votos totais e popularidade) presentes na tabela fato.

- **Integração com a Dimensão de Tempo (dim_tempo):**  
  A junção pelo campo `data_lancamento` com `data_completa` permite extrair os componentes temporais (ano, mês e dia) da data de lançamento da série. Isso possibilita análises temporais e valida que a extração de data foi feita de forma correta.

- **Integração com a Dimensão de Sentimento (dim_sentimento):**  
  Ao unir pelo campo `id_tmdb`, verificamos se os textos dos overviews das séries foram capturados corretamente, permitindo futuras análises de sentimento e texto.

- **Integração com a Dimensão de Elenco (dim_elenco):**  
  A consulta também une com a dimensão de elenco para exibir informações sobre os atores (nome do ator, personagem e popularidade) associados à série. Essa união ajuda a confirmar que os dados do elenco foram processados corretamente e estão relacionados à série correta.

## Por que essa consulta valida o modelo dimensional?

Esta consulta serve como uma **evidência prática** de que:
- As tabelas fato e dimensões estão interligadas corretamente através das chaves comuns (nesse caso, `id_tmdb` e `data_lancamento`).
- Os dados essenciais de cada entidade (série, tempo, sentimento e elenco) foram carregados e estão disponíveis para análises.
- É possível realizar joins entre as diferentes tabelas sem perder registros importantes, o que demonstra a integridade do modelo dimensional.

![consulta](../Evidencias/consulta.png)

## 6. Como Executar
1. Faça o upload do arquivo `refined_job.py` no AWS Glue Scripts (ou utilize um bucket S3 de scripts).  
2. Crie ou edite um Job no Glue, referenciando esse script.  
3. Configure as conexões, IAM Role e parâmetros necessários (ex.: `JOB_NAME`).  
4. Execute o Job.  
5. Acompanhe o progresso pelo console do Glue ou CloudWatch Logs.  
6. Ao finalizar, verifique o S3 na pasta `Refined/`.


