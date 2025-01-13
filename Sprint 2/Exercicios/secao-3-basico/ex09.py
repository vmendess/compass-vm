'''
Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, 
Truese a lâmpada estiver ligada, False caso esteja desligada. 

A classe Lampada possuí os seguintes métodos:
liga(): muda o estado da lâmpada para ligada
desliga(): muda o estado da lâmpada para desligada
esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

Para testar sua classe:
Ligue a Lampada
Imprima: A lâmpada está ligada? True
Desligue a Lampada
Imprima: A lâmpada ainda está ligada? False
'''

# Resolução:

class Lampada:
    def __init__(self, estado: bool):
        self.ligada = estado  # Sempre usar o mesmo nome de atributo

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self) -> bool:
        return self.ligada


# Testando a classe
lamp = Lampada(False)  # Inicialmente desligada
lamp.liga()
print('A lâmpada está ligada?', lamp.esta_ligada())  # Deve imprimir True