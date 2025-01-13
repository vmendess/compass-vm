Este **README** descreve o processo de Extração, Transformação e Carga (**ETL**) aplicado ao arquivo [`actors.csv`](actors.csv). O objetivo é analisar dados de atores e filmes, extraindo informações relevantes para gerar relatórios detalhados.

## Estrutura do Processo

O fluxo do processo ETL está dividido em etapas sequenciais, executadas pelo script [`menu_analise.py`](menu_analise.py). **É obrigatório executar o script [`funcoes_analise.py`](funcoes_analise.py) antes de rodar o menu interativo**, pois ele contém as funções essenciais para processar os dados.

## Passos Iniciais

1. **Certifique-se de que o arquivo [`actors.csv`](actors.csv) está na pasta correta.**
2. **Execute o script [`funcoes_analise.py`](funcoes_analise.py) para garantir que todas as funções necessárias estejam disponíveis.**
3. Após executar `funcoes_analise.py`, rode o script [`menu_analise.py`](menu_analise.py).

## Estrutura de Diretórios
```
Sprint 2/Exercicios/secao-6-ETL/
├── actors.csv
├── funcoes_analise.py  # Contém as funções necessárias para processar os dados
├── menu_analise.py  # Interface interativa para execução do ETL
├── resultados/
│   ├── etapa-1.txt
│   ├── etapa-2.txt
│   ├── etapa-3.txt
│   ├── etapa-4.txt
│   ├── etapa-5.txt
└── README.md
```

## Etapas do Processo ETL

O processo está dividido nas seguintes etapas, cada uma gerando um arquivo na pasta [`resultados/`](resultados/):

### **1️⃣ Criação da Estrutura de Diretórios**
Antes de executar qualquer etapa, é necessário garantir que a estrutura de diretórios esteja correta. Utilize a opção **7** no menu para criar a pasta [`resultados/`](resultados/) e os arquivos `.txt` necessários.

### **2️⃣ Execução das Etapas**

#### **Etapa 1 - Ator com mais filmes**
- Identifica o ator ou atriz com o maior número de filmes listados no dataset.
- **Arquivo de saída:** [`resultados/etapa-1.txt`](resultados/etapa-1.txt)
- **Exemplo de resultado:**
  ```
  O ator/atriz com maior número de filmes no dataset é Robert DeNiro, com 79 filmes.
  ```

#### **Etapa 2 - Média de Receita Bruta**
- Calcula a média de receita bruta gerada pelos filmes do dataset.
- **Arquivo de saída:** [`resultados/etapa-2.txt`](resultados/etapa-2.txt)
- **Exemplo de resultado:**
  ```
  A média de receita bruta dos principais filmes dos atores é de 256.45 milhões de dólares.
  ```

#### **Etapa 3 - Ator com Maior Receita Média por Filme**
- Identifica o ator ou atriz com maior média de receita por filme.
- **Arquivo de saída:** [`resultados/etapa-3.txt`](resultados/etapa-3.txt)
- **Exemplo de resultado:**
  ```
  O ator/atriz com maior média de receita bruta por filme é Leonardo DiCaprio, com 340.75 milhões de dólares por filme.
  ```

#### **Etapa 4 - Contagem de Filmes Mais Rentáveis**
- Lista os filmes que mais aparecem no dataset e suas respectivas contagens.
- **Arquivo de saída:** [`resultados/etapa-4.txt`](resultados/etapa-4.txt)
- **Exemplo de resultado:**
  ```
  1 - O filme The Avengers aparece 6 vezes no dataset.
  2 - O filme Catching Fire aparece 4 vezes no dataset.
  ```

#### **Etapa 5 - Atores Ordenados por Receita Total**
- Lista os atores ordenados por receita bruta total.
- **Arquivo de saída:** [`resultados/etapa-5.txt`](resultados/etapa-5.txt)
- **Exemplo de resultado:**
  ```
  1 - Tom Hanks - 5.2 bilhões de dólares.
  2 - Harrison Ford - 4.9 bilhões de dólares.
  ```

### **3️⃣ Execução Completa**
Para executar todas as etapas de uma só vez, utilize a opção **6** no menu.

## Observações Importantes
- Se a pasta [`resultados/`](resultados/) não existir, utilize a opção **7** no menu para criá-la automaticamente.
- **O script `menu_analise.py` não funcionará sem antes executar `funcoes_analise.py`**.
- Para futuras execuções, basta rodar novamente o script [`menu_analise.py`](menu_analise.py) e escolher a etapa desejada.

📌 **Este documento será atualizado conforme melhorias no processo ETL forem implementadas.**

