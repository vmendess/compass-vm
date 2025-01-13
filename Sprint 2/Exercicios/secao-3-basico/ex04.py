'''
Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. 
Utilize a lista a seguir para testar sua função.
['abc', 'abc', 'abc', '123', 'abc', '123', '123']
'''

# Resolução:

#Função:
def remover_duplicatas_sem_set(lista):
    # Criar uma lista vazia para armazenar elementos únicos
    lista_unica = []
    
    # Iterar sobre a lista original
    for elemento in lista:
        if elemento not in lista_unica:  # Verifica se o elemento já está na nova lista
            lista_unica.append(elemento)
    
    return lista_unica

#Teste da função com a lista de teste:

# Lista fornecida
lista_teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

# Testando a função
resultado = remover_duplicatas_sem_set(lista_teste)
print(resultado)
