# CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NUMEROS PARES QUE ESTÃO NO INTERVALO ENTRE 1 E 50
import time

print("Seguem todos os numeros pares de 0 a 50:")
print("=" * 40) 
time.sleep(1)

for n in range(0, 52, 2):
    print(f"Nº: {n}")
    time.sleep(0.35)
print("=" * 7)
print("ACABOU")
print("=" * 7)