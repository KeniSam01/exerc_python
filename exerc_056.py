# crie um programa que faça o computador jogar jokenpo com você.

import random

jokenpo = random.choices(["Pedra", "Papel", "Tesoura"], k=3)

usuario = str(input("Vamos jogar JOKENPO!!\nEscolha Pedra, Papel ou Tesoura e veja se consegue ganhar de mim!")).upper().strip()

if usuario == "PEDRA" and jokenpo[0] == "Pedra":
    print(f"Você escolheu {usuario} e eu também! EMPATAMOS.")
elif usuario == "PEDRA" and jokenpo[0] == "Papel":
    print(f"Você escolheu {usuario} e eu {jokenpo[0].upper()} GANHEI.")
elif usuario == "PEDRA" and jokenpo[0] == "Tesoura":
    print(f"Você escolheu {usuario} e eu {jokenpo[0].upper()} PERDI")

elif usuario == "PAPEL" and jokenpo[0] == "Pedra":
    print(f"Você escolheu {usuario} e eu {jokenpo[0].upper()} PERDI")
elif usuario == "PAPEL" and jokenpo[0] == "Papel":
    print(f"Você escolheu {usuario} e eu também! EMPATAMOS")
elif usuario == "PAPEL" and jokenpo[0] == "Tesoura":
    print(f"Você escolheu {usuario} e eu {jokenpo[0].upper()} GANHEI")

elif usuario == "TESOURA" and jokenpo[0] == "Tesoura":
    print(f"Você escolheu: {usuario} e eu também! EMPATAMOS")
elif usuario == "TESOURA" and jokenpo[0] == "Pedra":
    print(f"Você escolheu {usuario} e eu {jokenpo[0].upper()} GANHEI")
elif usuario == "TESOURA" and jokenpo[0] == "Papel":
    print(f"Você escolheu {usuario} e eu {jokenpo[0].upper()} PERDI")