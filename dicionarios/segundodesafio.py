dic_funcionarios = {"William":2000, "Mike":1900, "Dustin":1950, "Fernanda":2100, "Holly":2025}

cadastro_funcionario = input("coloque aqui o nome do funcionário")
cadastro_salario = input("coloque o salário que ele ira receber")
cadastro_salario = int(cadastro_salario)

if cadastro_funcionario in dic_funcionarios:
    print("esse funcionário já existe")
else: 
    print(f"o funcionário {cadastro_funcionario} foi cadastrado e receberá um salário de {cadastro_salario}")
    print("abaixo, veja a lista atual de funcionários")
    dic_funcionarios[cadastro_funcionario] = cadastro_salario

print(dic_funcionarios)