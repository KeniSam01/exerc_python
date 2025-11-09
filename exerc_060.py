# REFAÇA O DESAFIO 009 MOSTRANDO A TABUADA DE UM NUMERO QUE O USUARIO ESCOLHER SO QUE AGORA UTILIZANDO UM LAÇO FOR.

import time

print("=" * 23)
print("SUA-TABUADA-ONLINE.NET")
print("=" * 23)
time.sleep(1)
tabuada = int(input("DIGITE O NÚMERO QUE VOCÊ QUER CONSULTAR: "))
final = int(input("DIGITE ATÉ QUAL NÚMERO VOCÊ QUER SABER O MULTIPLICADOR: "))
print("=" * 23)
print("SUA-TABUADA-ONLINE.NET")
print("=" * 23)
time.sleep(1)
for numero in range(0, final + 1):

    print(f"{tabuada} X {numero} = {tabuada * numero}")
    print("=" * 15)
print("-- FIM --")
print("=" * 15)