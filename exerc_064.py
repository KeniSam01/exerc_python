# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES.
idades = []
contador_maior = 0
contador_menor = 0
for idade in range(0, 7):
    idade = int(input("Digite o ano de nascimento: "))
    idades == idades.append(idade)
    if idade <= 2007:
        contador_maior += 1
    else:
        contador_menor += 1

print(f"PARABÉNS,EXISTEM {contador_maior} PESSOAS QUE JÁ SÃO DE MAIOR!!")
print(f"INFELIZMENTE TEM {contador_menor} PESSOAS QUE AINDA SÃO MENORES!!!")
