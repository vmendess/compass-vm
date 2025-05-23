# Estrutura da Pasta Desafio

A pasta [`Desafio/`](Desafio/) está organizada da seguinte forma:

- [`notebook_jupyter/`](notebook_jupyter/) - Notebook Jupyter com o código de análise
- [`googleplaystore.csv`](googleplaystore.csv) - Dataset original utilizado na análise
- [`relatorio_valores_distintos.txt`](relatorio_valores_distintos.txt) - Relatório gerado com estatísticas detalhadas dos valores distintos das colunas
- [`README.md`](README.md) - Documentação do desafio

---
## Resumo do Desafio

O desafio envolveu a análise de dados da Google Play Store, utilizando Python, Pandas, utilizei o Matplotlib.pyplot para processamento e visualização. As etapas incluíram diagnóstico dos dados, limpeza, transformação e geração de gráficos para identificar padrões.

O principal desafio foi a construção de consultas e filtros eficientes para identificar valores inconsistentes com a lógica de cada coluna. Além disso, foi necessário tratar a conversão de tipos numéricos, remover dados despadronizados e ajustar a formatação dos gráficos. O uso do Pyplot exigiu refinamento para garantir uma apresentação visual clara e alinhada com os dados analisados.

A abordagem seguiu um fluxo estruturado, priorizando organização nos dados e visualizações diretas para a análise.

## Conjunto de Dados

O dataset utilizado é o [`googleplaystore.csv`](googleplaystore.csv), contendo informações sobre aplicativos disponíveis na Google Play Store. Esse conjunto de dados inclui atributos como nome do app, categoria, número de downloads, avaliações, tipo de monetização e classificação indicativa.

Quando visualizamos o arquivo .csv inicialmente, podemos identificar essa estrutura:

![Arquivo CSV](../Evidencias/google_play_store_csv.png)
---
## Etapas da Análise

### 1) Diagnóstico Inicial

Foram verificadas as colunas do dataset, identificando a necessidade de limpeza e transformação dos dados. A função `diagnostico_completo()` foi utilizada para listar e organizar as informações de cada coluna. O relatório gerado está disponível em [`relatorio_valores_distintos.txt`](relatorio_valores_distintos.txt), contendo:

- Lista dos valores distintos de cada coluna, organizados em ordem alfabética (A-Z)
- Contagem da frequência de cada valor
- Inclusão de valores nulos e sua respectiva quantidade
- Identificação de possíveis inconsistências nos dados, como caracteres especiais ou variações inesperadas

Por exemplo, a ordenação dos valores revelou um erro na coluna **Installs**. O valor Free foi detectado dentro dessa coluna, o que indica um possível erro de tipagem ou registro incorreto.

Coluna: Installs

Valor: Free, Repetições: 1

Esse valor não deveria estar presente nessa coluna, pois a coluna Installs deveria conter apenas números representando a quantidade de instalações.

A ordenação dos valores em ordem alfabética (A-Z) permite detectar rapidamente valores que fogem da lógica esperada.

![Relatório TXT](../Evidencias/relatorio_txt.png)
### 2) Limpeza dos Dados

Foram aplicadas as seguintes transformações:
- Remoção de linhas duplicadas.
- Conversão da coluna `Installs` para valores numéricos, removendo caracteres não numéricos.
- Conversão da coluna `Price`, retirando o símbolo `$` e transformando para tipo numérico.
- Conversão da coluna `Reviews` para tipo numérico, garantindo a coerência das análises.

### 3) Geração de Gráficos

Código fonte que gera o Top 5 Apps por Número de Instalações:
```python
# Selecionar os 5 apps com mais instalações
top_5_installs = df.nlargest(5, "Installs")

# Cores para cada barra
colors = ['#00FFAA', '#FF5733', '#FFD700', '#1E90FF', '#9B59B6']

# Gráfico estilizado com fundo dark
with plt.style.context('dark_background'):
    plt.figure(figsize=(14, 7))  

    # Gráfico de barras
    plt.bar(top_5_installs["App"], top_5_installs["Installs"], color=colors, edgecolor='white', linewidth=1.5)

    # Rótulos e título
    plt.xlabel("Apps", color='white', fontsize=14, fontweight='bold')
    plt.ylabel("Número de Instalações", color='white', fontsize=14, fontweight='bold')
    plt.title("Top 5 Apps por Número de Instalações", color='white', fontsize=16, fontweight='bold')

    # Rotação dos rótulos do eixo X
    plt.xticks(rotation=30, ha='right', fontsize=14, color='white')
    plt.yticks(fontsize=12, color='white')

    # Grid discreto
    plt.grid(axis='y', linestyle='--', alpha=0.5, color='gray')

    # Números acima das barras para destacar valores
    for i, v in enumerate(top_5_installs["Installs"]):
        plt.text(i, v + (v * 0.02), f'{v:,}', ha='center', fontsize=12, color='white', fontweight='bold')

    # Espaçamento inferior para evitar corte dos rótulos
    plt.subplots_adjust(bottom=0.25)

    # Gráfico
    plt.show()
```

Gráficos foram gerados para visualizar padrões nos dados. Os principais incluem:

#### **Top 5 Apps por Número de Instalações**
- Destacando os aplicativos mais populares com base no número de downloads.
- 1e9 é uma expressão em notação científica que significa 1 bilhão, ou seja, 1000000000. 
- A notação científica é uma forma de representar números muito grandes ou muito pequenos de forma que fiquem entre 1 e 10, multiplicados por uma potência de base 10. 
- As linguagens de programação utilizam a notação e ou E porque é mais fácil de digitar e imprimir do que um sobrescrito. Por exemplo, 1e-9 representa uma flutuação baixa, enquanto 1e9 representa uma flutuação alta. 

![Top 5 Instalações](../Evidencias/top_5_instalacao.png)

#### **Distribuição de Preços**
Demonstrando como os aplicativos pagos estão distribuídos em relação ao preço.

![Distribuição de Preços](../Evidencias/app_mais_caro_and_mature17.png)

#### **Cálculos Adicionais**
Gráficos que mostram cálculos adicionais para validar padrões nos dados.

![Cálculo Adicional 1](../Evidencias/calculo_adicional1.png)
![Cálculo Adicional 2](../Evidencias/calculo_adicional2.png)

#### **Distribuição de Apps por Categoria (Total: 34 categorias)**
Exibindo a frequência de cada categoria dentro do dataset.

![Distribuição de Categorias](../Evidencias/pie_chart.png)

#### **Avaliações e Review Score**
Análise dos top 10 aplicativos com melhores avaliações e pontuação.

![Top 10 Reviews](../Evidencias/top10_review.png)

### 4) Notebook Jupyter

A pasta [`notebook_jupyter/`](notebook_jupyter/) contém o código utilizado para processamento, análise e geração dos gráficos. Ele pode ser executado no Jupyter Notebook para reproduzir os resultados e realizar novas análises.

---
## Como Executar

Para reproduzir a análise e os gráficos no **Jupyter Notebook**, siga as etapas abaixo.

### 1. Configuração do Ambiente

Antes de executar o notebook, é necessário configurar o ambiente e instalar os pacotes necessários.

#### Requisitos:
- Python 3.x instalado ([Download](https://www.python.org/downloads/))
- Git instalado ([Download](https://git-scm.com/downloads))
- Jupyter Notebook instalado

**Instalação dos pacotes necessários:**
No terminal ou prompt de comando, execute:

```sh
pip install pandas matplotlib notebook
```

#### 2.Executando no ambiente
- Execute as células do notebook para carregar e processar os dados.

#### 3. Consulte o relatório de valores distintos em [`relatorio_valores_distintos.txt`](relatorio_valores_distintos.txt).

#### 4. Gráficos
- Visualize os gráficos e os resultados gerados dentro do notebook.


