idade = 22
nome = "Fernanda"
cor_preferida = "azul"

# primeira forma de concatenar textos, utilizando ","

# -- print("olá, seu nome é", nome, "você tem", idade, "anos, e sua cor preferida é", cor_preferida)

# segunda forma, escrevendo dentro de váriaveis e usando "+"

# texto_completo = "olá, seu nome é " + nome + " tem " + str(idade) + " anos " + "e sua cor preferida é..." + cor_preferida

# ~~ observação, não irá permitir calculos, e nem espaço automático nos inteiros.

# -- print(texto_completo)

# a melhor forma é utilizando váriaveis dentro do próprio texto, utilizando "f" depois do =

# texto_completo2 = f"olá, seu nome é {nome}, sua idade é de {idade} anos e sua cor preferida é a cor {cor_preferida}"

# print(texto_completo2)

email = " TAFODANECURSOR@GMAIL.COM "


email = email.strip()
email = email.capitalize()

print(email)
caracteres = len(email)

texto = f"olá, seu nome é {nome} e o seu email é {email} e a quantidade de caracteres do seu email é {caracteres}"

print(texto)

posicao = email.find("o")

print(posicao)

print(email[0:14])