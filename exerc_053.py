# refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:

# equilatero: todos os lados são iguais
# isosceles: dois lados iguais
# escaleno: todos os lados diferentes

r1 = float(input("Digite a primeira reta: "))
r2 = float(input("Digite a segunda reta: "))
r3 = float(input("Digite a terceira reta: "))

if r2 < r1 + r3 and r3 < r1 + r2 and r1 < r2 + r3:
    print("O triangulo pode se formar.")
    if r1 == r2 and r1 == r3 or r2 == r1 and r2 == r3 or r3 == r1 and r3 == r2:
        print("Pode se formar um triangulo equilatero.")
    elif r1 == r2 or r1 == r3 or r3 == r2 and r2 == r1 or r2 == r3 or r1 == r3 and r3 == r1 or r3 == r2:
        print("Pode se formar um triangulo isosceles.")
else:
    print("O triangulo não pode se formar")