'''
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:

Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
import random 
# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500),50)

Use as variáveis abaixo para representar cada operação matemática:
mediana
media
valor_minimo 
valor_maximo 

Importante: Esperamos que você utilize as funções abaixo em seu código:
random
max
min
sum
'''

# Resolução:

import random  # importando a biblioteca

# aleatoriamente 50 números de 0...500
random_list = random.sample(range(500), 50)

# ordena a lista
random_list.sort()

# calcula os valores solicitados
valor_minimo = min(random_list)
valor_maximo = max(random_list)
media = sum(random_list) / len(random_list)

# cálculo da mediana
meio = len(random_list) // 2
if len(random_list) % 2 == 0:  
    mediana = (random_list[meio - 1] + random_list[meio]) / 2
else:
    mediana = random_list[meio]

# imprimindo os resultados
print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
