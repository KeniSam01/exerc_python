# CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALINDROMO, DESCONSIDERANDO OS ESPAÇOS

frase = str(input("Digite uma frase: ")).upper()
frase_limpa = frase.replace(" ", "").upper()
frase_invertida = frase_limpa[::-1].upper()
print(f"O inverso de {frase_limpa} é {frase_invertida}")
if frase_invertida == frase_limpa:
    print("E o texto é um palindromo")
else:
    print("O texto não é um palindromo.")