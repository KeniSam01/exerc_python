# REFAÇA O DESAFIO 51 LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE

print("=" * 20)
print("TERMOS DE PROG. ARIT.")
print("=" * 20)

numero = int(input("Digite um numero para saber sua P.A: "))
razao = int(input("Digite a razão: "))
termo = numero
contador = 1
while contador <= 10:
    print(f"{termo} -> ", end="")
    termo += razao
    contador += 1
print("FIM")
