# escreva um programa que leia a velocidade de um carro

# se ele ultrapassar 80km/h mostre a uma mensagem dizendo que ele foi multado

# a multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = float(input("Digite a velocidade que o carro passou: "))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f"Sua velocidade foi de: {velocidade:.0f}km\nE a multa é de R${multa:.0f} reais")
else:
    print(F"A velocidade de {velocidade:.0f}km está dentro do limite!!")