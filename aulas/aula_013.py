# laços for

for c in range(0, 10): # EXEMPLO CLASSICO DE UMA ESTRUTURA FOR
    print(f"numero: {c}")
print("=" * 10)
print("Acabou a contagem!")
print("=" * 10)

for contagem in range(1, 6): #o ultimo ele ignora, ou seja, vai de 1 a 5 NESTE CASO
    print("Oi")
print("=" * 10)
print("FIM")
print("=" * 10)

for numero in range(1, 6, 2): # NESTE EXEMPLO ELE PULA DUAS CASAS
    print(f"numero: {numero}")
print("Este exemplo ele vai de 1 ao 5 pulando DUAS casas!!")
print("<EXEMPLO 3 FINALIZADO>")

n = int(input("Digite um numero: ")) # EXEMPLO COM INTERAÇÃO DO USUARIO
for num in range(0, n):
    print(num)

inicio = int(input("inicio: ")) # EXEMPLO COM O USUARIO ESCOLHENDO TODAS AS OPÇÕES
fim = int(input("Fim: "))
passo =int(input("Passo: "))
for numero in range(inicio, fim, passo):
    print(numero)

s = 0
for n in range(0 , 3): # NESTE EXEMPLO PEDIMOS VALORES E SOMAMOS TODOS OS VALORES DIGITADOS
    c = int(input("Digite um valor: "))
    s += c
print(f"O somatorio de todos os valores foi: {s}")

# CONSEGUIMOS UTILIZAR A ESCOLHA DO USUARIO COM OPERAÇÕES MATEMATICAS 