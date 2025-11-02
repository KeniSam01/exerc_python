#escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão:

# 1 para binario
# 2 para octal
# 3 para hexadecimal

n = int(input("Digite um numero: "))
escolha = int(input("Escolha a base de conversão:\n1 - binario\n2 - octal\n3 - hexadecimal\n"))
if escolha == 1:
    binario = bin(n)
    print(f"O numero conertido para binario fica: {binario}")
elif escolha == 2:
    octal = oct(n)
    print(f"O numero convertido para octal fica: {octal}")
elif escolha == 3:
    hex = hex(n)
    print(f"O numero convertido para hexadecimal fica: {hex}")