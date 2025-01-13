'''
Dada a seguinte lista:
 a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
 Faca um programa que gere uma nova lista contendo apenas numeros impares.
'''

# Resolução:

# Lista original
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Criar uma lista vazia para armazenar os números ímpares
impares = []

# Usar um loop for para iterar pela lista original
for i in a:
    # Verificar se o número é ímpar
    if i % 2 != 0:
        # Adicionar o número à lista se for ímpar
        impares.append(i)

# Exibir o resultado
print(impares)