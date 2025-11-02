# deselvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo.

reta1 = float(input("Digite a primeira reta: "))
reta2 = float(input("Digite a segunda reta: "))
reta3 = float(input("Digite a terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta1 + reta2:
    print("O triangulo pode se formar.")
else:
    print("o triangulo não pode se formar.")