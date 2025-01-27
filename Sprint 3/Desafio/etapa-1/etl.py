import pandas as pd

# Caminhos de entrada e saída
INPUT_PATH = '/volume_input/concert_tours_by_women.csv'  # Volume montado da etapa-1
OUTPUT_PATH = '/volume_output/csv_limpo.csv'  # Volume montado da etapa-2

def analisar_dados():
    """
    Lê o CSV original e exibe todas as linhas.
    Exibe também os tipos de cada coluna.
    """
    # Lê o arquivo CSV
    df = pd.read_csv(INPUT_PATH, delimiter=',', engine='python')

    # Exibe todas as linhas do DataFrame
    pd.set_option("display.max_rows", None)

    print("\n=== Análise do CSV (todas as linhas) ===\n")
    print(df)

    # Exibe os tipos de cada coluna
    print("\nTipos de dados das colunas:\n", df.dtypes)
    print("\n=== Fim da análise ===\n")

    # Retorna a configuração de exibição para o padrão (opcional)
    pd.reset_option("display.max_rows")


def limpar_csv():
    """
    Limpa o arquivo CSV original e salva um novo arquivo formatado.
    """
    df = pd.read_csv(INPUT_PATH, delimiter=',', engine='python')

    # Limpeza de Tour title
    df['Tour title'] = (
        df['Tour title']
        .str.replace(r'â€', '', regex=True)
        .str.replace(r'\[\d+\]\[.\]', '', regex=True)
        .str.replace(r'\*', '', regex=True)
        .str.replace(r'[†‡]', '', regex=True)  # remove símbolos † e ‡
        .str.strip()
    )

    # Corrige "BeyoncÃ©" para "Beyoncé"
    df['Artist'] = df['Artist'].str.replace('BeyoncÃ©', 'Beyoncé', regex=False)

    # Converte colunas monetárias
    monetary_cols = ['Actual gross', 'Adjusted gross (in 2022 dollars)', 'Average gross']
    for col in monetary_cols:
        if df[col].dtype == object:
            df[col] = df[col].str.replace(r'[^\d.]', '', regex=True)
        df[col] = df[col].astype(float)

    # Separa 'Year(s)' em 'Start Year' e 'End Year'
    df[['Start Year', 'End Year']] = df['Year(s)'].str.split('-', expand=True)
    df['End Year'] = df['End Year'].fillna(df['Start Year'])

    # Reordenar colunas
    final_cols = [
        'Rank', 'Actual gross', 'Adjusted gross (in 2022 dollars)',
        'Artist', 'Tour title', 'Shows', 'Average gross',
        'Start Year', 'End Year'
    ]
    df = df[final_cols]

    # Salvar com delimitador ";" para o Excel reconhecer como colunas
    df.to_csv(OUTPUT_PATH, index=False, encoding='utf-8-sig', sep=';')
    print(f"Salvo: {OUTPUT_PATH}")


if __name__ == '__main__':
    analisar_dados()
    limpar_csv()
