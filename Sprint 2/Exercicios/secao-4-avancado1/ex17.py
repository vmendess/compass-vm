'''
Implemente uma classe chamada Calculo que contenha um método que aceita dois parâmetros, x e y, e retorne a soma dos dois.

Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, x e y, e retorne a subtração dos dois (resultados negativos são permitidos).

Utilize os valores abaixo para testar seu exercício:

x = 4
y = 5

Imprima:

Somando: 4+5 = 9
Subtraindo: 4-5 = -1
'''

# Resolução:

class Calculo:
    def somar(self, x, y):
        return x + y
    
    def subtrair(self, x, y):
        return x - y

# testando a classe
x = 4
y = 5
calc = Calculo()

# imprimindo a soma e a subtracao com format
print(f'Somando: {x}+{y} = {calc.somar(x, y)}')
print(f'Subtraindo: {x}-{y} = {calc.subtrair(x, y)}')
