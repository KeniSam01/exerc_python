# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA Progressão Aritmetica. NO FINALMOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO

print("=" * 20)
print("10 TERMOS DE UMA PA")
print("=" * 20)
p_termo = int(input("Digite o 1º TERMO: "))
razao = int(input("Digite a RAZÃO: "))
decimo = p_termo + (10 - 1) * razao
for n in range(p_termo, decimo + razao, razao):
    print(f"{n}", end='-> ')
print("-- FIM --")