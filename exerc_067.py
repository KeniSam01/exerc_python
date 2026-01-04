# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES "M" OU "F". CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO.

s = 1
while s != 0:
    sexo = str(input("Digite seu sexo (M/F): ")).upper()
    if sexo in "Mm " or sexo in "Ff":
        print("Sexo registrado com sucesso!")
    else:
        print("Sexo invalido.\nDigite novamente.")