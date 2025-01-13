'''
A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. 
Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 
Abaixo apresentando uma possível entrada para a função.
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]
A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. 
Na lista anterior, por exemplo, teríamos como resultado final 200.
Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:
reduce (módulo functools)
map
'''

# Resolução:

from functools import reduce

def calcula_saldo(lancamentos) -> float:
    # o map() percorre a lista e:
    # se for crédito 'C', mantém o valor positivo
    # se for débito 'D', transforma em negativo
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    
    # usamos reduce() pra somar tudo e obter o saldo final
    saldo = reduce(lambda acc, x: acc + x, valores, 0)
    return saldo

# comeca com 0
    # 0 + (-200)  == -200
    # -200 + 300  == 100
    # 100 + 100   == 200
    # saldo = 200

# exemplo de uso
lancamentos = [(200, 'D'), (300, 'C'), (100, 'C')]
print(calcula_saldo(lancamentos))  # saída: 200
