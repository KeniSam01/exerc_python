# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# se ele ainda vai se alistar ao serviço militar

# se é a hora de se alistar

#se ja passou do tempo do alistamento.

# seu programa tambem devera mostrar o tempo que falta ou que passou do prazo

idade = int(input("Digite o seu ano de nascimento: "))
maioridade = 2025 - idade

if maioridade == 18:
    print(f"Você tem que ir se alistar antes que complete 18 anos.")
elif maioridade < 18:
    print(f"Você ainda é jovem para se alistar.\nFaltam {18 - maioridade} ano(s) para você se alistar.")
else:
    print(f"Você passou do tempo de se alistar.\nVoce passou {maioridade - 18} anos do prazo")