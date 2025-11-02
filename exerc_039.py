# escreva um programa que faça o computador pensar em um numero inteiro de 0 a 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador

# o programa devera escrever na tela se o usuario venceu ou perdeu.

import random

numero = random.randint(0, 5)

escolha = int(input("Escolha um numero de 0 à 5: "))
if escolha == numero:
    print(f"Parabés, você escolheu o {escolha} e acertou o numero que o computador escolheu!! ")
else:
    print(f"Infelizmente você errou!!\nvocê escolheu o numero {escolha} e o numero escolhido pelo computador foi {numero}, mas você pode tentar novamente!!!")