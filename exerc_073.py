# ESCREVA UM PROGRAMA QUE LEIA UM NUMERO N INTEIRO QUALQUER E MOSTRE NA TELA OS N PRIMEIROS ELEMENTOS DE UMA SEQUENCIA DE FIBONACCI

# EX:
# 0 - 1 - 1 - 2 - 3 - 5 - 8 

primeiro_valor = 0
segundo_valor = 1
termos = int(input("Digite quantos elementos de FIBONACCI você quer: "))
contador = 2
print(f"SEQUENCIA DE FIBONACCI")
print("~=" * 10)
print(f"{primeiro_valor} -> {segundo_valor} -> ", end="")
while contador < termos:
    terceiro_valor = primeiro_valor + segundo_valor # CRIAMOS O TERCEIRO NUMERO DA SEQUENCIA
    primeiro_valor = segundo_valor # ATUALIZAMOS O PRIMEIRO VALOR, PARA QUE O LOOP ATUALIZE AUTOMATICAMENTE E CRESÇA
    segundo_valor = terceiro_valor # ATUALIZAMOS O SEGUNDO VALOR, PARA QUE COM O LOOP ELE ATUALIZE AUTOMATICAMENTE E CRESÇA
    print(f"{terceiro_valor} -> ", end="")
    contador += 1 # CONTADOR APENAS PARA CONTAR QUANTOS TERMOS VAI APARECER
print(f"FIM\nVOCÊ QUERIA {termos} TERMOS")
