# a confederação nacional de natação precisa de um programa que leia o ano de nascimento e mostre sua categoria de acorco com sua idade:

# ate 9 anos: mirim
# ate 14 anos: infantil
# ate 19 anos: junior
# ate 20 anos: senior
# acima: master

ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2025 - ano_nascimento
if idade <= 9:
    print(f"Você tem {idade} anos\nE sua categoria é: MIRIM")
elif idade > 9 and idade <= 14:
    print(f"Você tem {idade} anos\nE sua categoria é: INFANTIL")
elif idade > 14 and idade <= 19:
    print(f"Você tem {idade} anos\nE sua categoria é: JUNIOR")
elif idade > 19 and idade <= 20:
    print(f"Você tem {idade} anos\nE sua categoria é: SENIOR")
elif idade > 20:
    print(f"Você tem {idade} anos\nE sua categoria é: MASTER")