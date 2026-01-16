# calcular o aumento de salários, com a mesma regra de antes, salários de <= 1000(aumento de 10%) e > 1000(aumento de 15%), porém, juntar tudo no final.

lista_salarios = [500, 300, 700, 800, 950, 1500, 2800, 5000, 4900, 6000]

total_aumento = 0

for salario in lista_salarios:
    if salario < 800:
        aumento_salarial = 0.10
    else: 
        aumento_salarial = 0.15
    
    aumento = salario * aumento_salarial + salario
    
    print(f"seu salário era {salario} e agora é: {aumento}")
    total_aumento = total_aumento + aumento

print(f"o total de salário pago ao todo é: {total_aumento}")