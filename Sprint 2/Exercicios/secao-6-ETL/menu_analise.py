"""
Menu interativo para análise de atores
"""
import os
from funcoes_analise import (
    etapa_1, etapa_2, etapa_3, etapa_4, etapa_5,
    executar_todas_etapas, criar_arquivos_txt
)

def menu():
    """Menu interativo para escolher qual etapa executar"""
    base_path = 'Sprint 2/Exercicios/secao-6-ETL'
    
    while True:
        print("\n=== Menu de Análise de Atores ===")
        print("1. Ator com mais filmes")
        print("2. Média de receita bruta")
        print("3. Ator com maior média por filme")
        print("4. Contagem de filmes mais rentáveis")
        print("5. Lista ordenada por receita total")
        print("6. Executar todas as etapas")
        print("7. Criar pasta e arquivos necessários")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '0':
            break
        
        if opcao == '7':
            pasta_resultados = criar_arquivos_txt(base_path)
            print(f"Arquivos criados em: {pasta_resultados}")
        else:
            arquivo_csv = os.path.join(base_path, 'actors.csv')
            pasta_resultados = os.path.join(base_path, 'resultados')
            
            if not os.path.exists(pasta_resultados):
                print("\nPasta 'resultados' não encontrada!")
                print("Por favor, use a opção 7 primeiro para criar a estrutura necessária.")
                continue
            
            if opcao == '6':
                executar_todas_etapas(base_path)
            elif opcao in ['1', '2', '3', '4', '5']:
                etapa = [etapa_1, etapa_2, etapa_3, etapa_4, etapa_5][int(opcao)-1]
                caminho_saida = os.path.join(pasta_resultados, f'etapa-{opcao}.txt')
                etapa(arquivo_csv, caminho_saida)
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    menu()