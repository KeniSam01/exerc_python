# FAÇA UM PROGRAMA QUE LEIA UM NUMERO QUALQUER E MOSTRE O SEU FATORIAL.

# EX:
#5! = 5X4X3X2X1 = 120

num = int(input("Digite um numero para saber seu fatorial: "))
c = num
f = 1
print(f"Calculando {num}! = ", end="")
while c > 0:
    print(f"{c}", end="")
    print(f" X " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print(f)