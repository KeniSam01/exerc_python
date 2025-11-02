# escreva um programa para aprovar o emprestimo bancario para compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.

# calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario ou senão o emprestimo sera negado.

valor = float(input("Digite o valor da casa: "))
salario = float(input("Qual seu salario? "))
anos = int(input("Quantos anos você pretende pagar? "))

parcela = valor / (anos * 12)
limite = (salario * 30) / 100
if parcela > limite:
    print("O parcelamento excedeu o valor limite, assim não conseguimos liberar a compra.")
else:
    print(f"Seu emprestimo foi aprovado!!!\nVocê terá parcelas de: R${parcela:.0f} reais")