'''
Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.
Teste sua função com os seguintes parâmetros:
(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
'''
# Resolução:

def print_parametros(*args, **kwargs):
    for valor in args:  # Imprime cada parâmetro não nomeado
        print(valor)
    
    for valor in kwargs.values():  # Imprime apenas os valores dos parâmetros nomeados
        print(valor)

# Teste com os parâmetros fornecidos
print_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

