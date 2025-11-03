# crie um programa que faça o computador jogar jokenpo com você.

import time
import random

jokenpo = random.choices(["Pedra", "Papel", "Tesoura"], k=3)

usuario = str(input("Vamos jogar JOKENPO!!\nEscolha Pedra, Papel ou Tesoura e veja se consegue ganhar de mim!\nEscolha:")).upper().strip()

if usuario == "PEDRA" and jokenpo[0] == "Pedra":
    print("Analisando sua escolha...")
    time.sleep(1.5)
    print(f"Você escolheu: {usuario}\nE eu também!\n\033[7;30;40mEMPATAMOS.\033[7;30;40m")
elif usuario == "PEDRA" and jokenpo[0] == "Papel":
    print("Analisando sua escolha...")
    time.sleep(1.5)
    print(f"Você escolheu: {usuario}\nE eu: {jokenpo[0].upper()}\n\033[1;31mGANHEI.\033[1;31m")
elif usuario == "PEDRA" and jokenpo[0] == "Tesoura":
    print("Analisando sua escolha...")
    time.sleep(1.5)
    print(f"Você escolheu: {usuario}\nE eu: {jokenpo[0].upper()}\n\033[1;32mPERDI.\033[1;32m")

elif usuario == "PAPEL" and jokenpo[0] == "Pedra":
    print("Analisando sua escolha...")
    time.sleep(1.5)
    print(f"Você escolheu: {usuario}\nE eu: {jokenpo[0].upper()}\n\033[1;32mPERDI\033[1;32m")
elif usuario == "PAPEL" and jokenpo[0] == "Papel":
    print("Analisando sua escolha...")
    time.sleep(1.5)
    print(f"Você escolheu: {usuario}\nE eu também!\n\033[7;30;40mEMPATAMOS\033[7;30;40m")
elif usuario == "PAPEL" and jokenpo[0] == "Tesoura":
    print("Analisando sua escolha...")
    time.sleep(1.5)
    print(f"Você escolheu: {usuario}\nE eu: {jokenpo[0].upper()}\n\033[1;31mGANHEI\033[1;31m")

elif usuario == "TESOURA" and jokenpo[0] == "Tesoura":
    print("Analisando sua escolha...")
    time.sleep(1.5)
    print(f"Você escolheu: {usuario}\nE eu também!\n\033[7;30;40mEMPATAMOS\033[7;30;40m")
elif usuario == "TESOURA" and jokenpo[0] == "Pedra":
    print("Analisando sua escolha...")
    time.sleep(1.5)
    print(f"Você escolheu: {usuario}\nE eu: {jokenpo[0].upper()}\n\033[1;31mGANHEI\033[1;31m")
elif usuario == "TESOURA" and jokenpo[0] == "Papel":
    print("Analisando sua escolha...")
    time.sleep(1.5)
    print(f"Você escolheu: {usuario}\nE eu: {jokenpo[0].upper()}\n\033[1;32mPERDI\033[1;32m")