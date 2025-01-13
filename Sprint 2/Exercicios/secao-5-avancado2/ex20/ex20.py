'''
Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. 
Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
Você deverá aplicar as seguintes funções no exercício:
map
filter
sorted
sum

Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
a lista dos 5 maiores números pares em ordem decrescente;
a soma destes valores.
'''

# Resolução:

# caminho do arquivo
caminho_arquivo = 'Sprint 2/Exercicios/secao-5-avancado2/ex20/number.txt'

# lendo o arquivo e extraindo os números
with open(caminho_arquivo, 'r') as file:
    numbers = list(map(int, file.readlines()))

# filtrar apenas os números pares
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# ordenar em ordem decrescente e pegar os 5 maiores valores
top_5_evens = sorted(even_numbers, reverse=True)[:5]

# calcular a soma dos 5 maiores valores
sum_top_5 = sum(top_5_evens)

# exibir os resultados
print(top_5_evens)
print(sum_top_5)
