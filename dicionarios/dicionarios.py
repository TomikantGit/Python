lista_nomes = ["Fernanda", "Alice", "Kaynan", "Delrion"]
lista_idades = [22, 21, 20, 22]

dic_pessoas = {"Fernanda":22, "Alice":21, "Kaynan":20, "Delrion":22}

# pegar item do dicionário

print(dic_pessoas["Alice"])

# também funciona com mais de um valor

dic_dinheiro = {"Cartão": [200, 1500, 120], "Dinheiro_Físico": [120, 146, 2000], "Pix": [1700, 2000, 3000]}

print(dic_dinheiro["Pix"])

# adicionar valor

dic_dinheiro["Cartão"] = dic_dinheiro["Cartão"] + [600, 580, 100]

print(dic_dinheiro["Cartão"])

# remover um item

dic_dinheiro.pop("Pix")

print(dic_dinheiro)

# editar um valor



# verifica se existe no dicionario

pessoa_existe = "Fernanda" in dic_pessoas

print(pessoa_existe)

# verifica se existe atráves da chave/key ou o valor/value

print("Fernanda" in dic_pessoas.keys())
print(22 in dic_pessoas.values())

# mostrar as chaves ou valores como listas.

lista_pessoas = list(dic_pessoas.keys())
print(lista_pessoas)
lista_idades = list(dic_pessoas.values())
print(lista_idades)

# mostrando a quantidade de itens no dicionário

qtd_pessoas = len(dic_pessoas)
print(qtd_pessoas)