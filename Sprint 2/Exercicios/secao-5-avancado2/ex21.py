'''
def conta_vogais(texto:str)-> int: Utilizando high order functions, implemente o corpo da função conta_vogais. 
O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.
É obrigatório aplicar as seguintes funções:
- len
- filter
- lambda

Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.
'''

# Resolução:

def conta_vogais(texto: str) -> int:
    return len(list(filter(lambda x: x in 'aeiouAEIOU', texto)))

# Exemplos de uso
print(conta_vogais('Olá, Mundo!'))  # saída esperada: 3, como a vogal 'a' está com acento não vai reconhecer
print(conta_vogais('Python'))       # saída esperada: 1
print(conta_vogais('ABCDE'))        # saída esperada: 2
print(conta_vogais('xyz'))          # saída esperada: 0
