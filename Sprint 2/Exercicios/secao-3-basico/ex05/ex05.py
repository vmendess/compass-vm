# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
# Dica: leia a documentação do pacote json

# Resolução:
import json

# Caminho relativo corrigido
with open('Sprint 2/Exercicios/secao-3-basico/ex05/person.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Exibir o conteúdo do JSON
print(dados)



