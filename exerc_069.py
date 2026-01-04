# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:

'''[1] SOMAR
   [2] MULTIPLICAR
   [3] MAIOR
   [4] NOVOS NUMEROS
   [5] SAIR DO PROGRAMA
   
SEU PROGRAMA DEVERA REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO'''

n1 = int(input("Digite o 1º valor: "))
n2 = int(input("Digite o 2º valor: "))

escolha = 0

while True:
    escolha_usuario = int(input(('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA
                                
    ESCOLHA UMA DAS OPÇÕES: ''')))

    if escolha_usuario == 1:
        print(f"Resultado: {n1 + n2}")
        break
    elif escolha_usuario == 2:
        print(f"Resultado: {n1 * n2}")
        break
    elif escolha_usuario == 3:
        if n1 > n2:
            print(f"O numero {n1} é maior que o numero {n2}")
            break
        else:
            print(f"O numero {n2} é maior que o numero {n1}")
            break
    elif escolha_usuario == 4:
        n1 = int(input("Digite novamente o primeiro valor: "))
        n2 = int(input("Digite novamente o segundo valor: "))
    else:
        print("Programa encerrado.")
        break

