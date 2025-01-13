"""
Funções para análise do arquivo actors.csv
"""
import os
'''
O módulo os faz parte da biblioteca padrão do Python (não é uma biblioteca de análise de dados)
e está sendo utilizado apenas para:
Manipular caminhos de arquivos e pastas (por exemplo, os.path.join para montar caminhos corretamente, 
independente do sistema operacional).
Verificar e criar diretórios (com funções como os.path.exists e os.makedirs).
'''

caminho_arquivo = 'Sprint 2/Exercicios/secao-6-ETL/actors.csv'
caminho_saida = 'Sprint 2/Exercicios/secao-6-ETL/etapa-1/etapa-1.txt'

print('Funcoes carregadas com sucesso! ')

def ler_arquivo(caminho_arquivo):
    """Lê o arquivo CSV e retorna as linhas"""
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        return arquivo.readlines()

def processar_linha(linha):
    """Processa uma linha tratando casos com vírgula no nome"""
    valores = linha.strip().split(',')
    if len(valores) > 6:  # Caso com vírgula no nome
        return [valores[0] + ',' + valores[1]] + valores[2:]
    return valores

def salvar_resultado(caminho_saida, conteudo):
    """Salva o resultado em arquivo"""
    with open(caminho_saida, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
    print(f'Resultado salvo em: {caminho_saida}!')

def criar_arquivos_txt(base_path):
    """Cria a pasta de resultados e os arquivos .txt necessários"""
    # Cria a pasta de resultados se não existir
    pasta_resultados = os.path.join(base_path, 'resultados')
    if not os.path.exists(pasta_resultados):
        os.makedirs(pasta_resultados)
    
    # Cria os arquivos .txt
    for i in range(1, 6):
        arquivo_txt = os.path.join(pasta_resultados, f'etapa-{i}.txt')
        if not os.path.exists(arquivo_txt):
            with open(arquivo_txt, 'w', encoding='utf-8') as f:
                pass  # Cria um arquivo vazio
    
    print("Pasta 'resultados' e arquivos criados com sucesso!")
    return pasta_resultados

def etapa_1(caminho_arquivo, caminho_saida):
    """Encontra ator/atriz com maior número de filmes"""
    linhas = ler_arquivo(caminho_arquivo)
    dados = linhas[1:]  # Pula cabeçalho
    
    maior_filmes = 0
    ator_mais_filmes = ""
    
    for linha in dados:
        valores = processar_linha(linha)
        try:
            num_filmes = int(float(valores[2]))  # Number of Movies é a terceira coluna
            if num_filmes > maior_filmes:
                maior_filmes = num_filmes
                ator_mais_filmes = valores[0]
        except ValueError:
            continue
    
    resultado = f"o ator/atriz com maior número de filmes no dataset é {ator_mais_filmes}, com {maior_filmes} filmes."
    salvar_resultado(caminho_saida, resultado)

def etapa_2(caminho_arquivo, caminho_saida):
    """Calcula média de receita de bilheteria bruta"""
    linhas = ler_arquivo(caminho_arquivo)
    dados = linhas[1:]  # Pula cabeçalho
    
    valores_gross = []
    for linha in dados:
        valores = processar_linha(linha)
        try:
            gross = float(valores[-1])  # Último valor é o Gross
            valores_gross.append(gross)
        except ValueError:
            continue
    
    media_gross = sum(valores_gross) / len(valores_gross)
    resultado = f'a média de receita bruta dos principais filmes dos atores é de {media_gross:.2f} milhões de dólares.'
    salvar_resultado(caminho_saida, resultado)

def etapa_3(caminho_arquivo, caminho_saida):
    """Encontra ator/atriz com maior média de receita por filme"""
    linhas = ler_arquivo(caminho_arquivo)
    dados = linhas[1:]  # Pula cabeçalho
    
    melhor_ator = ''
    maior_media = 0.0
    
    for linha in dados:
        valores = processar_linha(linha)
        try:
            media_filme = float(valores[3])  # Average per Movie é a quarta coluna
            if media_filme > maior_media:
                maior_media = media_filme
                melhor_ator = valores[0]
        except ValueError:
            continue
    
    resultado = f'ator/atriz com maior média de receita bruta por filme: {melhor_ator}, com {maior_media:.2f} milhões de dólares por filme.'
    salvar_resultado(caminho_saida, resultado)

def etapa_4(caminho_arquivo, caminho_saida):
    """Conta aparições dos filmes de maior bilheteria"""
    linhas = ler_arquivo(caminho_arquivo)
    dados = linhas[1:]  # Pula cabeçalho
    
    contagem_filmes = {}
    for linha in dados:
        valores = processar_linha(linha)
        filme = valores[4]  # #1 Movie é a quinta coluna
        contagem_filmes[filme] = contagem_filmes.get(filme, 0) + 1
    
    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))
    
    resultado = []
    for i, (filme, quantidade) in enumerate(filmes_ordenados, 1):
        vez_ou_vezes = "vez" if quantidade == 1 else "vezes"
        resultado.append(f'{i} - O filme {filme} aparece {quantidade} {vez_ou_vezes} no dataset.')
    
    salvar_resultado(caminho_saida, '\n'.join(resultado))

def etapa_5(caminho_arquivo, caminho_saida):
    """Lista atores ordenados por receita bruta total"""
    linhas = ler_arquivo(caminho_arquivo)
    dados = linhas[1:]  # Pula cabeçalho
    
    dados_atores = []
    for linha in dados:
        valores = processar_linha(linha)
        try:
            nome_ator = valores[0]
            receita_total = float(valores[1])  # Total Gross é a segunda coluna
            dados_atores.append((nome_ator, receita_total))
        except ValueError:
            continue
    
    dados_atores.sort(key=lambda x: x[1], reverse=True)
    
    resultado = []
    for ator, receita in dados_atores:
        resultado.append(f"{ator} - {receita:.2f}")
    
    salvar_resultado(caminho_saida, '\n'.join(resultado))

def executar_todas_etapas(base_path):
    """Executa todas as etapas em sequência"""
    arquivo_csv = os.path.join(base_path, 'actors.csv')
    pasta_resultados = os.path.join(base_path, 'resultados')
    
    etapas = [etapa_1, etapa_2, etapa_3, etapa_4, etapa_5]
    
    for i, func in enumerate(etapas, 1):
        print(f'\nExecutando etapa {i}...')
        caminho_saida = os.path.join(pasta_resultados, f'etapa-{i}.txt')
        func(arquivo_csv, caminho_saida)
