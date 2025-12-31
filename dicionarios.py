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

# editar um valor

print(dic_dinheiro)
