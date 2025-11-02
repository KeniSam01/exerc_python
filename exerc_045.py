# escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento

# para salarios superiores a R$ 1.250,00 calcule um aumento de 10%

# para os inferiores ou iguais, o aumento é de 15%

salario = float(input("Digite seu salario: "))
if salario > 1250:
    print(f"Seu salario teve um aumento de 10%!!\nSendo assim, passará a ser: R${salario + (salario *0.10)} reais")
else:
    print(f"Seu salario teve um aumento de 15%!!\nNisso seu salario passará a ser: R${salario + (salario * 0.15)} reais")