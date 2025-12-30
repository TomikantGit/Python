# para criar uma lista, apenas abra e feche colchetes dentro da variavel

lista_idades = [18, 19, 25, 30, 15, 22]
lista_nomes = ["Pedro", "João", "Lucas", "Ana", "Maria"]

# cada item na lista tem um índice de 0 a infinito igual os textos.

print(lista_idades[1])  

# len também funciona para ver a quantidade de itens na lista

print(len(lista_idades))

# funções básicas: sum, min, max

print(sum(lista_idades))
print(min(lista_idades))
print(max(lista_idades))

# também pode ser guardado dentro de váriaveis.

# verifica se existe na lista retornando true ou false

print(18 in lista_idades)

# retorna o indice

posicao_idade = lista_idades.index(18)

print(posicao_idade)

# editar um item de uma lista

lista_produtos = ["banana", "maçã", "laranja"]

lista_produtos[0] = "morango"

print(lista_produtos)

# metodo remove e pop para remover itens de lista

# remove | remove o item pelo nome escrito

lista_produtos.remove("laranja")

print(lista_produtos)

# remove pelo índice

lista_produtos.pop(0)

print(lista_produtos)   

# adicionando itens a lista com append.

lista_nomes.append("Fernanda")

print(lista_nomes)

# adicionando itens de uma outra lista na lista original com extend

lista_nomes2 = ["Wita", "Will", "Cristiano"]

lista_nomes.extend(lista_nomes2)

print(lista_nomes)