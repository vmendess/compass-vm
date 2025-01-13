'''
Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. 
Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.
Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.
'''

# Resolução:

def my_map(lista, f):
    resultados = []  # Lista vazia para armazenar os resultados
    
    for elemento in lista:  # Itera sobre cada elemento da lista
        resultados.append(f(elemento))  # Aplica a função e adiciona à lista
    
    return resultados  # Retorna a lista transformada

# Função de teste: potência de 2
def potencia_de_2(n):
    return n ** 2

# Lista de entrada
entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Chamando a função my_map
resultado = my_map(entrada, potencia_de_2)

# Exibir resultado
print(resultado)

