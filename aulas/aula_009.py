# manipulando cadeia de caracteres(textos)
# fatiamento

frase = "Olá, eu sou o João"

print(frase)
print(frase[9:16]) # Fatia determinado range de caracteres
print(frase[:4]) # Começo do caractere zero[0]
print(frase[15:]) # Fatia do [15] até o final da string
print(frase[2::3]) # Começa do [2] e vai até o final, pulando 3 casas.

#analisar uma string

print(len(frase)) # conta quantos caracteres tem
print(frase.count("o")) # conta quantas vezes tem determinado caractere
print(frase.find("o"))

#Transformação

print(frase.replace("João", "Caio")) # o primeiro campo é para identificar o que você quer que mude, e o segundo é a palavra que você quer colocar no lugar.

print(frase.upper()) # transforma tudo em maiusculo
print(frase.lower()) # transforma tudo em minusculo
print(frase.capitalize()) # Deixa apenas a primeira letra da palavra em maiusculo
print(frase.title()) # deixa todas as primeiras letras de todas as palavras da string em maisculo
print(frase.strip()) # remove espaços inuteis no começo e no fim da string
print(frase.rstrip()) # remove os ultimos espaços inuteis
print(frase.lstrip()) # remove os espaços inuteis do começo

# Dividir Strings

print(frase.split(" ")) # divide a string numa lista
print("~".join(frase)) # junta uma lista numa string