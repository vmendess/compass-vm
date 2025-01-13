'''
Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
Dica: leia a documentação da função open(...)
'''

# Resolução:

# Caminho do arquivo
caminho_arquivo = 'Sprint 2/Exercicios/secao-3-basico/ex07/arquivo_texto.txt'

# Função para ler o conteúdo do arquivo
def ler_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()

# Exibe o conteúdo do arquivo
print(ler_arquivo(caminho_arquivo), end='')

"""
Em um ambiente como a Udemy, o arquivo já está disponível no sistema,
então basta referenciá-lo pelo nome. Na IDE, é necessário especificar
o caminho completo para garantir que o Python encontre o arquivo corretamente.
"""

