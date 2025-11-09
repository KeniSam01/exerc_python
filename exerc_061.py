# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NUMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FORAM PARES. SE O VALOR DIGITADO POR IMPAR DESCONSIDERE-O
print("=" * 30)
print("CALCULADORA DE NUMEROS PARES")
print("=" * 30)
soma = 0
for c in range(0, 6):
    numero = int(input("Digite um valor: "))
    if numero % 2 == 0:
        soma = soma + numero
print(f"A soma dos numeros é: {soma}")