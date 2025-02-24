## Estrutura de Pastas
A pasta **Sprint 5** está organizada da seguinte forma:

```
Sprint 5/
├─ Certificados/  # Certificados conquistados durante a sprint, Obtivemos certificados da AWS nessa sprint
├─ Desafio/       # Implementações relacionadas ao desafio da sprint
├─ Evidencias/    # Imagens que comprovam a execução das atividades do desafio
├─ Exercicios/    # Scripts e resoluções dos exercícios
└─ README.md      # Documentação da Sprint 5
```

---

## Certificados

Os certificados obtidos durante a Sprint 5 estão disponíveis na pasta [Certificados](Certificados/). Obtivemos certificados da AWS nesta sprint.

---
### Desafio

A pasta **Desafio** contém todos os artefatos relacionados ao desafio desta sprint. A estrutura está organizada para facilitar o entendimento das entregas e inclui os seguintes itens:

- **1 Arquivo README.md nas duas etapas**: Documentação detalhada sobre o desafio, incluindo as etapas e os resultados obtidos.
- **etapa-1/**: Artefatos da Etapa 1 – preparação do ambiente e upload dos arquivos CSV para o Amazon S3.
- **etapa-2/**: Artefatos da Etapa 2 – processamento dos dados e upload dos arquivos JSON para o Amazon S3.

---

## Evidências

As evidências para validação das execuções realizadas estão armazenadas na pasta [Evidencias](Evidencias/). Esta pasta contém capturas de tela e outros registros que comprovam a execução das atividades da sprint.

Exemplo de evidência gerada:

![json](./Evidencias/json_s3.png)

---

## Exercícios

Os exercícios foram organizados seguindo a estrutura do PB.

### Exercício 1: Processamento de Dados com Apache Spark e Docker

- **Objetivo:** Contar palavras em um README.md via Spark em container Docker.

### Exemplo das etapas para realização do primeiro exercicio:

#### **Etapa 1 - Download da Imagem Docker**
Para iniciar o processo, foi realizado o pull da imagem Docker necessária para rodar o ambiente Spark:

```sh
docker pull jupyter/all-spark-notebook
```

Essa imagem contém o Apache Spark e o Jupyter Lab pré-configurados.

#### **Etapa 2 - Criação e Execução do Container**
Após baixar a imagem, foi criado e iniciado um container Docker a partir da imagem `jupyter/all-spark-notebook`:

```sh
docker run -p 8888:8888 \
  -v "${PWD}/notebooks:/home/jovyan/work" \
  -v "${PWD}/data:/home/jovyan/data" \
  --name spark-container \
  jupyter/all-spark-notebook
```

O container foi configurado para expor a porta `8888`, permitindo acesso ao **Jupyter Lab** pelo navegador.

## Exercício 2: API TMDB

### 2.1. Etapa 1 - Criando sua conta no TMDB

1. Acesse o portal: [https://www.themoviedb.org/](https://www.themoviedb.org/)  
2. Clique em **Junte-se ao TMDB** na barra de navegação.  
3. Preencha o formulário de inscrição e clique em **Registrar** (use seu e-mail pessoal).  
4. Confirme seu e-mail seguindo as instruções recebidas.  
5. Faça login, clique no seu avatar (canto superior direito) e selecione **Visão geral** → **Editar Perfil**.  
6. No menu **API**, clique em **Criar** e selecione o tipo **Developer**.  
7. Preencha o formulário (pode usar dados fictícios) e informe no campo **Resumo** o objetivo do seu app.  
8. Em **Tipo de Uso**, selecione **Pessoal**.  

### 2.2. Etapa 2 - Testando rapidamente as credenciais e a biblioteca

Este exercício consiste na consulta de dados sobre filmes utilizando a API do **The Movie Database (TMDB)**. O meu objetivo foi buscar os **20 filmes mais bem avaliados**, exibindo título, data de lançamento, votos e média de avaliações.

### Exemplo das etapas para realização do segundo exercicio:

### **2.1. Configuração do Ambiente**

#### **Passo 1: Criar e ativar o ambiente virtual**
```sh
python -m venv venv
# Ativar no Windows (PowerShell)
venv\Scripts\Activate
# Ativar no Windows (CMD)
venv\Scripts\activate.bat
# Ativar no Linux/macOS
source venv/bin/activate
```

#### **Passo 2: Criar o arquivo `.env` e adicionar as credenciais da API TMDB**
```
API_KEY=XXXXXX
TOKEN_API=XXXXXX
```
---

