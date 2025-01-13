## Estrutura de Pastas
A pasta **Sprint 2** está organizada da seguinte forma:

```
Sprint 2/
├─ Certificados/  # Certificados conquistados durante a sprint
├─ Desafio/       # Implementações e análises relacionadas ao desafio da sprint
├─ Evidencias/    # Imagens que comprovam a execução das atividades do desafio
├─ Exercicios/    # Scripts e resoluções dos exercícios práticos
└─ README.md      # Documentação da Sprint 2
```

---

## Certificados

Os certificados obtidos durante a Sprint 2 estão disponíveis na pasta [Certificados](Certificados/). Não obtivemos certificados da AWS nesta sprint.

---
### Desafio

A pasta **[Desafio](Desafio/)** contém todos os artefatos relacionados ao desafio desta sprint. A estrutura está organizada para facilitar o entendimento das entregas e inclui os seguintes itens:

- **[README.md](Desafio/README.md)**: Documentação detalhada sobre o desafio, incluindo as etapas e os resultados obtidos.
- **[notebook_jupyter/](Desafio/notebook_jupyter/)**: Arquivos de notebooks contendo as implementações e análises de dados.
- **[googleplaystore.csv](Desafio/googleplaystore.csv)**: Arquivo utilizado para análise, contendo os dados brutos.
- **[relatorio_valores_distintos.txt](Desafio/relatorio_valores_distintos.txt)**: Relatório detalhado com estatísticas sobre os valores distintos das colunas do dataset.

---

## Evidências

As evidências para validação das análises e execuções realizadas estão armazenadas na pasta [Evidencias](Evidencias/). Esta pasta contém capturas de tela e outros registros que comprovam a execução das atividades da sprint.

Exemplo de evidência gerada a partir da análise:

![Relatório TXT](Evidencias/relatorio_txt.png)

---

## Exercícios

Os exercícios foram organizados seguindo a estrutura do curso na Udemy e contemplam diferentes níveis de complexidade.

### Seção 3: Básico
Nesta seção, os exercícios abordam fundamentos essenciais de lógica de programação e manipulação de listas em Python.

**Exemplo de Código:**
[Ex01](Exercicios/secao-3-basico/ex01.py)
```python
# Dada a seguinte lista:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Criar uma nova lista contendo apenas números ímpares
impares = []
for i in a:
    if i % 2 != 0:
        impares.append(i)
print(impares)
```

### Seção 4: Avançado 1
Essa seção foca no aprofundamento de conceitos como funções de alta ordem e manipulação de strings.

**Exemplo de Código:**
[Ex15](Exercicios/secao-4-avancado1/ex15.py)
```python
# Implementação intermediária do exercício
# Exemplo de lógica avançada será inserida conforme necessidade
```

### Seção 5: Avançado 2
Exercícios avançados que envolvem conceitos mais complexos de programação funcional e processamento de dados.

**Exemplo de Código:**
[Ex21](Exercicios/secao-5-avancado2/ex21.py)
```python
def conta_vogais(texto: str) -> int:
    """
    Conta o número de vogais em um texto, utilizando filter e lambda.
    """
    return len(list(filter(lambda x: x in 'aeiouAEIOU', texto)))

print(conta_vogais('Python'))
print(conta_vogais('ABCDE'))
print(conta_vogais('xyz'))
```

### Seção 6: ETL
Essa seção é voltada para **Extração, Transformação e Carga de Dados**, explorando manipulação de arquivos e automação de processos.

**Exemplo de Código:**
[menu_Analise](Exercicios/secao-6-ETL/menu_analise.py)
```python
import os

def menu():
    """Menu interativo para análise de atores"""
    print("\n=== Menu de Análise de Atores ===")
    print("1. Ator com mais filmes")
    print("2. Média de receita bruta")
    print("3. Ator com maior média por filme")
    print("4. Contagem de filmes mais rentáveis")
    print("5. Lista ordenada por receita total")
    print("6. Executar todas as etapas")
    print("7. Criar pasta e arquivos necessários")
    print("0. Sair")
    opcao = input("\nEscolha uma opção: ")
    return opcao
```

---

