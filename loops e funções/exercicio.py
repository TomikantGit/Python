# salário de até 1000 aumentam 10%, salários acima de 1000 recebem 15%

lista_salario = [800, 750, 2000, 3000, 4000, 999, 1000]

for salario in lista_salario: 
    if salario <= 1000:
        salario_novo = salario * 0.10 + salario
        print(f"seu salário antigo era {salario} e agora será {salario_novo}")
    elif salario > 1000:
        salario_mais_mil = salario * 0.15 + salario
        print(f"e o salários que era acima de 1000, como {salario}, agora será de {salario_mais_mil}")
    