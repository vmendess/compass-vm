import random
import time
import os
import names

# Define a semente para reprodução dos resultados
random.seed(40)

# Define os parâmetros do dataset
qtd_nomes_unicos = 39080
qtd_nomes_aleatorios = 10000000

# Lista vazia que receberá os nomes únicos
nomes_unicos = []

# Gerando nomes únicos
print('Gerando nomes únicos...')
for _ in range(qtd_nomes_unicos):
    nomes_unicos.append(names.get_full_name())

print(f'Total de nomes únicos gerados: {len(nomes_unicos)}')

# Gerando nomes aleatórios com base nos únicos
nomes_aleatorios = []
print('Gerando nomes aleatórios...')
for _ in range(qtd_nomes_aleatorios):
    nomes_aleatorios.append(random.choice(nomes_unicos))

# Salvando os nomes no arquivo "nomes_aleatorios.txt"
with open('Sprint 6/Exercicios/parte-1-massa-dados/etapa-3/nomes_aleatorios.txt', 'w', encoding='utf-8') as arquivo:
    for nome in nomes_aleatorios:
        arquivo.write(nome + '\n')

print('Arquivo nomes_aleatorios.txt criado com sucesso!')
