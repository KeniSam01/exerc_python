# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NUMEROS IMPARES QUE SÃO MULTIPLOS DE TRES E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500.
n = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        n += c 
print(f" Foram encontrados {contador} numeros\n E a soma deles é: {n}")

