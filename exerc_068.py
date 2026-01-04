# MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI "PENSAR" EM UM NUMERO DE 0 A 10. SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSARIOS PARA VENCER.

import random
import time

print("=" * 25)
print("JOGO DA ADVINHAÇÃO V2.0")
print("=" * 25)
time.sleep(2)
tentativas = 0
numero = random.randint(0, 10)
escolha = int(input("Tente adivinhar o numero que o computador escolheu: "))
tentativas += 1
while escolha != numero:
    escolha = int(input("INFELIZMENTE VOCÊ ERROU, TENTE NOVAMENTE: "))
    tentativas += 1
if escolha == numero:
    print(f"PARABÉNS!!! \nO COMPUTADOR ESCOLHEU O Nº: {numero} \nE VOCÊ ACERTOU COM: {tentativas} TENTATIVAS!!")