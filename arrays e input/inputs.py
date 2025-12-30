# para colocar um input para que o usuário possa escrever, é necessário colocar o nome "input" após o = e escrever o prompt/pergunta para o úsuario

nome = input("Digite seu nome aqui! ")
idade = input("Me diga sua idade ")

# quando for lidar com inteiros, coloque o nome da variavel, e após o =, coloque o tipo que quer transformar.
idade = int(idade)

texto_apresentacao = f"olá, seu nome é {nome} e sua idade é {idade} certo?"

print(texto_apresentacao)

# testes abaixo

salario_pedro = input("digite seu salário ")
salario_pedro = int(salario_pedro)
salario_wita = input("digite seu salário ")
salario_wita = int(salario_wita)

salario_unificado = salario_wita + salario_pedro

print(salario_unificado)