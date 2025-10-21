preco = float(input("Qual o preço do produto? "))
desconto = preco - (preco * 5 / 100)
print(f"O seu produto está com 5% de desconto! de R$ {preco} por apenas R$ { desconto:.2f}")