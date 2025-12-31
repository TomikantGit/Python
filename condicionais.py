nome = input("Digite o nome do usuário")
idade = input(f"digite a idade da {nome} ")
idade = int(idade)

# para criar uma condição, esta deve ser a estrutura, else não recebe condição, significando literalmente: caso contrário, nunca esquecer de dar tab.

# if idade >= 18:
#     print("ela é maior de idade")
# else: 
#     print("ela é menor de idade")

# funciona também com lista

# lista_nomes = ["João", "Kaynan", "Delrion", "Akilles", "Will"]

# nome_enviado = input("digite um nome para adicionar a lista ")

# if nome_enviado in lista_nomes:
#     print("esse nome já existe.")
# else: lista_nomes.append(nome_enviado)

# print(lista_nomes)

# agora com elif

if nome == "Fernanda":
    print("Este é o nome correto!")
elif nome == "Pedro":
    print("este nome também é o correto!")
else: 
    print("nome errado")