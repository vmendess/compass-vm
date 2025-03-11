# Lista com 20 animais
animais = [
    'hipopótamo', 'pinguim', 'água-viva', 'raposa', 'camelo',
    'tubarão', 'borboleta', 'castor', 'esquilo', 'gorila',
    'lontra', 'pato', 'baleia', 'foca', 'urso-polar',
    'veado', 'canguru', 'guaxinim', 'morcego', 'rinoceronte'
]

# Ordena a lista em ordem crescente
animais.sort()

# Imprime cada animal usando list comprehension
[print(animal) for animal in animais]

# Grava cada animal em uma linha do arquivo 'animais.txt, nomes como: "água-viva", ficam no final pela codificação usada UTF-8'
with open('Sprint 6/Exercicios/parte-1-massa-dados/etapa-2/animais.txt', 'w', encoding='utf-8') as arquivo:
    for animal in animais:
        arquivo.write(animal + '\n')

print('Arquivo animais.txt criado com sucesso!')
