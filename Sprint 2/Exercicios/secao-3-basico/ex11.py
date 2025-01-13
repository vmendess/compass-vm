'''
Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
'''

# Resolução:

def dividir_lista(lista):
    tamanho = len(lista) // 3
    
    lista_1 = lista[:tamanho]
    lista_2 = lista[tamanho:2*tamanho]
    lista_3 = lista[2*tamanho:]

    return lista_1, lista_2, lista_3  # Retorna as três listas separadamente

# Teste com a lista fornecida
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
resultado = dividir_lista(lista)

# 🔹 Imprime as listas separadamente
print(*resultado)  # Isso imprimirá: [1, 2, 3, 4] [5, 6, 7, 8] [9, 10, 11, 12]
