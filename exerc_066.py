# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE:

# A MEDIA DE IDADE DO GRUPO
# QUAL É O NOME DO HOMEM MAIS VELHO
# QUANTAS MULHERES TEM MENOS DE 20 ANOS.

soma_idade = 0
media_idade = 0
maioridade_homem = 0
nome_velho = ""
tot_mulher_20 = 0
for item in range(0, 4):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo (M/F):  "))
    soma_idade += idade
    if item == 1 and sexo in "Mm":
        maioridade_homem = idade
        nome_velho = nome
    if sexo in "Mm" and idade > maioridade_homem:
       maioridade_homem = idade
       nome_velho = nome
    if sexo in "Ff" and idade < 20:
        tot_mulher_20 += 1

media_idade = soma_idade / 4
print(f"A media de idade do grupo é de {media_idade} anos")
print(f"O homem mais velho tem {maioridade_homem} anos e se chama {nome_velho}")
print(f"Ao todo são {tot_mulher_20} mulheres com menos de 20 anos")