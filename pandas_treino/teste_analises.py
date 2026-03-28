import pandas as pd

# importando a tabela

df = pd.read_csv('pandas_treino/dataset_vendas_10000_registros.csv')

# pegando as primeiras e últimas linhas da tabela

primeiras_linhas = df.head()
ultimas_linhas =  df.tail()

# analise descritiva de toda a tabela 

analise_descritiva = df.describe()

# filtros 

vendedor_bruno = df['vendedor'] == 'Bruno'
vendas_acima2k = df['lucro'] > 3000

relatorio_bruno = df[(vendedor_bruno) & (vendas_acima2k)]

# print(relatorio_bruno)

# operações dentro de agrupamento

relatorio_vendedores = df.groupby('vendedor')['lucro'].sum()

print(relatorio_vendedores)

# teste filtro em grupo

vendas_acima900k = relatorio_vendedores['lucro'] >= 9000000
relatorio_vendedores_milhao = relatorio_vendedores[vendas_acima900k]

print(relatorio_vendedores_milhao)