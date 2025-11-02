# crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

numero = int(input("Digite um numero: "))
if numero % 2 == 0:
    print(f"{numero} é PAR.")
else:
    print(f"{numero} é IMPAR.")