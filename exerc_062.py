# FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E DIGA SE ELE É OU NÃO UM NUMERO PRIMO

numero = int(input("Digite um numero: "))
tot = 0
for n in range(1, numero + 1):
    if numero % n == 0:
        print('\033[34m', end="")
        tot += 1
    else:
        print('\033[m', end="")
    print(n, end="")
print(f"\nO numero {numero} foi divisivel {tot} vezes")
if tot > 2:
    print(f"O numero não é primo")
else:
    print(f"O numero é primo")