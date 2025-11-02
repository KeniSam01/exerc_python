# desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 ate 30 sobrepeso
# 30 ate 40: obesidade
# acima de 40: obesidade morbida 

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Você tem um IMC de: {imc:.1f}\nPortanto está abaixo do peso!!")
elif imc >= 18.5 and imc <= 25:
    print(f"Voce tem um IMC de: {imc:.1f}\nPortanto está no seu peso ideal.")
elif imc >= 25 and imc <= 30:
    print(f"Você tem um IMC de: {imc:.1f}\nPortanto esta com sobrepeso. ")
elif imc > 30 and imc <= 40:
    print(f"Voce tem um IMC de: {imc:.1f}\nPortanto está com obesidade.")
else:
    print(f"Seu IMC passa dos 40\nPortanto está com obesidade morbida.")