import random

# Cria uma lista vazia
numeros = []

# Adiciona 250 números inteiros aleatórios entre 1 e 1000 à lista
for _ in range(250):
    numeros.append(random.randint(1, 1000))

# Inverte a ordem da lista
numeros.reverse()

# Exibe a lista invertida
print(numeros)
