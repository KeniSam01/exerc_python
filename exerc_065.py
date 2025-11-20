# FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS, NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS.
quant = []

for c in range(0, 5):
    peso = float(input("Digite o peso: "))
    quant == quant.append(peso)
print(f"A pessoa mais leve pesa: {min(quant)}KG")
print(f"E a pessoa mais pesada pesa: {max(quant)}KG")