'''
Implemente duas classes, Pato e Pardal, que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.
Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.
Imprima no console exatamente assim:

Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu
'''

# Resolução:

# classe-pai
class Passaro:  
    def voar(self):
        print('Voando...')
    
    def emitir_som(self):
        pass

#sub-classes:
class Pato(Passaro):  # herda os metódos da classe-pai
    def emitir_som(self):
        print('Pato emitindo som...')
        print('Quack Quack')

class Pardal(Passaro):
    def emitir_som(self):
        print('Pardal emitindo som...')
        print('Piu Piu')

# imprimindo os resultados conforme pede a questão
print('Pato')
pato = Pato()
pato.voar()
pato.emitir_som()

print('Pardal')
pardal = Pardal()
pardal.voar()
pardal.emitir_som()
