# calcular o aumento de salários, com a mesma regra de antes, salários de <= 1000(aumento de 10%) e > 1000(aumento de 15%), porém, juntar tudo no final.

lista_salarios = [500,300,700,800,950,1500,2800,5000,4900,6000]

for salario in lista_salarios:
    if salario <= 1000:
        aumento = 0.10
    elif salario > 1000:
        aumento = 0.15
        salario_novo = salario * aumento
        print(f"seu salario antigo erá {salario} e agora: {salario_novo}")
