import pandas as pd

# # abrir documento csv
# df = pd.read_csv('dataset_vendas_10000_registros.csv')

# #pegar as 5 primeiras linhas do documento
# primeiras_linhas = pd.DataFrame.head(df)

# #pegar as últimas 5 linhas
# ultimas_linhas = pd.DataFrame.tail(df)

# print(primeiras_linhas)
# print(ultimas_linhas)

funcionarios = {"Pessoas": ["Pedro", "Wita", "Fernanda", "Alice", "Will", "Kaynan", "Delrion"],
                "Salário": [1900,2400,3000,2700,4500,3650,2800]
                }

tabela = pd.DataFrame(funcionarios)

primeiras_linhas = pd.DataFrame.head(tabela)

print(tabela)

print(primeiras_linhas)