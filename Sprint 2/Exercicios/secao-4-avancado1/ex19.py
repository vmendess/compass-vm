'''
Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.
Defina o atributo cor de sua classe, de maneira que todas as instâncias de sua classe Avião sejam da cor "azul".
Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.
Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:

"O avião de modelo x possui uma velocidade máxima de y, capacidade para z passageiros e é da cor w."
Sendo x, y, z e w cada um dos atributos da classe Avião.

Valores de entrada:
modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul
modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul
modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul
'''

# Resolução:

class Aviao:
    cor = 'Azul'  # atributo da classe (compartilhado por todas as instâncias)

    def __init__(self, modelo, velocidade_maxima, capacidade):
        """Inicializa um avião com modelo, velocidade máxima e capacidade."""
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade

# criando a lista de avioes
avioes = [
    Aviao('BOIENG456', 1500, 400),
    Aviao('Embraer Praetor 600', 863, 14),
    Aviao('Antonov An-2', 258, 12)
]

# imprimindo os resultados
for aviao in avioes:
    print(f'O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima} km/h, '
          f'capacidade para {aviao.capacidade} passageiros e é da cor {Aviao.cor}.')

