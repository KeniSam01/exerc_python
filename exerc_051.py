# crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida.

# media abaixo de 5.0: REPROVADO

# media entre 5.0 e 6.9: RECUPERAÇÃO

# media 7.0 ou superior: APROVADO

n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite sua outra nota: "))
media = (n1 + n2) / 2
if media <= 5:
    print(f"Com a media {media}\nVocê foi reprovado.")
elif media >= 5 and media <= 6.9:
    print(f"Com a media {media}\nVoce ficou de recuperação")
elif media >= 7:
    print(f"Com a media {media}\nVoce foi aprovado!!")