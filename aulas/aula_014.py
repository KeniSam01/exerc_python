# ESTRUTURA DE REPETIÇÃO WHILE

# A ESTRUTURA DE REPETIÇÃO WHILE É UTILIZADA PARA REPETIR UM BLOCO DE CÓDIGO ENQUANTO UMA CONDIÇÃO FOR VERDADEIRA.

# USAMOS FOR QUANDO SABEMOS O LIMITE

# USAMOS WHILE QUANDO NÃO SABEMOS O LIMITE

# Se a condição for falsa logo na primeira verificação, o bloco nunca será executado. 

n = 1

while n < 20:
    print(n)
    n += 3

c = 1
par = impar = 0
while c != 0:
    c = int(input("Digite um valor: "))
    if c != 0:
        if c % 2 == 0:
            par += 1
        else:
            impar += 1

print(f"Você digitou {par} numeros pares e {impar} numeros impares")

