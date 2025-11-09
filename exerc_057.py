# FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFICIO. INDO DE 10 ATÉ 0 COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES.

import time
import emoji

print("CONTAGEM REGRESSIVA PARA O ANO NOVO!!!!")
print("=" * 40)
time.sleep(1)
for c in range(10, 0, -1):
    print(f"FALTAM {c} SEGUNDOS!!!")
    time.sleep(1)
print("=" * 22)
print(f"{emoji.emojize(":fireworks:")} FELIZ ANO NOVO!! {emoji.emojize(":fireworks:")}")
print("=" * 22)