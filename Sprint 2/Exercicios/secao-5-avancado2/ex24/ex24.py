'''
Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. 
Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, 
no intervalo [0-10]. 
É o arquivo estudantes.csv de seu exercício.

Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em 
formato textual contendo as seguintes informações:
Nome do estudante
Três maiores notas, em ordem decrescente
Média das três maiores notas, com duas casas decimais de precisão

O resultado do processamento deve ser escrito na saída padrão (print), 
ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:
Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>

Exemplo:
Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33

Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
round
map
sorted
'''

# Resolução: 

# caminho do arquivo
caminho_arquivo = 'Sprint 2/Exercicios/secao-5-avancado2/ex24/estudantes.csv'

# leitura do arquivo
with open(caminho_arquivo, 'r', encoding='utf-8') as file:
    linhas = file.readlines()

# processamento dos dados 
alunos = []
for linha in linhas[1:]:  # coloquei [1:] para ignorar o cabeçalho
    partes = linha.strip().split(',')
    nome = partes[0]
    notas = list(map(int, partes[1:]))  # converte notas para inteiros
    top3 = sorted(notas, reverse=True)[:3]  # pega as 3 maiores
    media = round(sum(top3) / 3, 2)  # calcula a média com 2 casas decimais
    alunos.append((nome, top3, media))

# ordenação por nome
alunos.sort(key=lambda x: x[0])

# imprimindo o resultado com format
for nome, notas, media in alunos:
    print(f'Nome: {nome} Notas: {notas} Média: {media}')



