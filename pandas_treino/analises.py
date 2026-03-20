import pandas as pd

tabela = pd.read_csv('pandas_treino/netflix_titles.csv')

primeiras_linhas = pd.DataFrame.head(tabela)
ultimas_linhas = pd.DataFrame.tail(tabela)
analise_descritiva = pd.DataFrame.describe(tabela)

infos_importantes = tabela[['title', 'type', 'duration']] # cria uma tabela separada 

print()

tipo_filmes = infos_importantes[infos_importantes['type'] == 'TV Show'] # mostra apenas as linhas da tabela que seja 

print(tipo_filmes)


