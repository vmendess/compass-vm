import os
import pandas as pd
import matplotlib.pyplot as plt

# Caminhos de entrada e saída
CAMINHO_CSV = '/volume/csv_limpo.csv'  # CSV gerado pela etapa-1
CAMINHO_SAIDA_RESPOSTAS = '/volume/respostas.txt'
CAMINHO_SAIDA_GRAFICOS = '/volume/graficos/'

# Garante que a pasta para salvar os gráficos exista
os.makedirs(CAMINHO_SAIDA_GRAFICOS, exist_ok=True)

# Carrega o arquivo CSV limpo
df = pd.read_csv(CAMINHO_CSV, delimiter=';', engine='python')

# Configura o tema escuro para os gráficos
plt.style.use('dark_background')

# Q1: Artista com maior média de faturamento bruto (Actual gross)
q1_artista = (
    df.groupby('Artist')['Actual gross']
    .mean()
    .idxmax()
)
q1_resposta = f"Q1:\n--- {q1_artista}\n"

# Q2: Turnê com maior média de faturamento bruto em um único ano (Average gross)
turnes_unico_ano = df[df['Start Year'] == df['End Year']]
if not turnes_unico_ano.empty:
    q2_turne = turnes_unico_ano.loc[turnes_unico_ano['Average gross'].idxmax(), ['Tour title', 'Average gross']]
    q2_resposta = f"Q2:\n--- {q2_turne['Tour title']} (${q2_turne['Average gross']:,.2f})\n"
else:
    q2_resposta = "Q2:\n--- Nenhuma turnê foi realizada em um único ano.\n"

# Q3: 3 artistas que mais lucraram com menos shows
q3_resultado = (
    df.groupby(['Artist', 'Tour title'], as_index=False)
    .agg({'Adjusted gross (in 2022 dollars)': 'sum', 'Shows': 'sum'})
    .sort_values(by=['Shows', 'Adjusted gross (in 2022 dollars)'], ascending=[True, False])
    .head(3)
)
q3_resposta = "Q3:\n"
for _, row in q3_resultado.iterrows():
    q3_resposta += f"--- {row['Artist']} | {row['Tour title']} (${row['Adjusted gross (in 2022 dollars)']:,.2f})\n"

# Salva as respostas em um arquivo de texto
with open(CAMINHO_SAIDA_RESPOSTAS, 'w', encoding='utf-8') as arquivo_respostas:
    arquivo_respostas.write(q1_resposta)
    arquivo_respostas.write(q2_resposta)
    arquivo_respostas.write(q3_resposta)

print(f"Respostas Q1, Q2 e Q3 salvas em: {CAMINHO_SAIDA_RESPOSTAS}")

# Q4: Gráfico de linhas do faturamento por ano para a artista que mais aparece
artista_mais_presente = df['Artist'].value_counts().idxmax()
faturamento_por_ano = (
    df[df['Artist'] == artista_mais_presente]
    .groupby('Start Year')['Actual gross']
    .sum()
)

plt.figure()
faturamento_por_ano.plot(kind='line', marker='o', color='cyan', linewidth=2)
plt.title(f"Faturamento por Ano - {artista_mais_presente}", fontsize=14, color='white')
plt.xlabel('Ano', fontsize=12, color='white')
plt.ylabel('Faturamento Bruto', fontsize=12, color='white')
plt.xticks(fontsize=10, color='white')
plt.yticks(fontsize=10, color='white')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig(f"{CAMINHO_SAIDA_GRAFICOS}Q4.png")
print("Gráfico Q4 salvo como 'Q4.png'")

# Q5: Gráfico de colunas com as 5 artistas com mais shows
artistas_com_mais_shows = (
    df.groupby('Artist')['Shows']
    .sum()
    .nlargest(5)
)

plt.figure()
artistas_com_mais_shows.plot(kind='bar', color='orange', edgecolor='white')
plt.title("Top 5 Artistas com Mais Shows", fontsize=14, color='white')
plt.xlabel('Artista', fontsize=12, color='white')
plt.ylabel('Total de Shows', fontsize=12, color='white')
plt.xticks(rotation=45, fontsize=10, color='white')  # Rotação para evitar sobreposição
plt.yticks(fontsize=10, color='white')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig(f"{CAMINHO_SAIDA_GRAFICOS}Q5.png")
print("Gráfico Q5 salvo como 'Q5.png'")
