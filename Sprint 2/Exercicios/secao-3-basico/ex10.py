'''
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. 
Depois imprima a soma dos valores.

A string deve ter valor  "1,3,4,6,10,76"
'''

# Resolução:

def soma_numeros(numeros: str) -> int:
    lista_numeros = [int(i) for i in numeros.split(',')]  # Divide a string e converte para inteiros
    return sum(lista_numeros)

# Teste
valores = '1,3,4,6,10,76'
resultado = soma_numeros(valores)

# **Imprimindo apenas o número da soma**
print(resultado)  # Deve imprimir a soma que neste caso é 100
