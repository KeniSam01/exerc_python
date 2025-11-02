# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# a vista dinheiro/cheque: 10% de desconto
# a vista no cartao: 5% de desconto
# em ate 2x no cartao: preço normal
# 3x ou mais no cartao: 20% de juros

valor_produto = float(input("Digite o valor do produto: "))
opcoes = int(input(f"""Escolha uma das opções: 
1 - A vista dinheiro/cheque: 10% de desconto
2 - A vista no cartao: 5% de desconto
3 - Em ate 2x no cartao: preço normal
4 - 3x ou mais no cartao: 20% de juros: """))

if opcoes == 1:
    desconto = valor_produto - ((valor_produto * 10) / 100)
    print(f"O produto custa R${valor_produto} e com o desconto de 10% fica R${desconto}")
elif opcoes == 2:
    cartao = valor_produto - ((valor_produto * 5) / 100)
    print(f"O produto custa R${valor_produto} e com o desconto de 5% fica R${cartao}")
elif opcoes == 3:
    print(f"O produto parcelado em 2X no cartão fica o preço normal dele de: R${valor_produto}")
elif opcoes == 4:
    juros = valor_produto + ((valor_produto * 20) / 100)
    print(f"O valor do produto pago em 3X no cartão de credito tem um acrescimo de 20% de juros\nSaindo de R${valor_produto} para R${juros}")