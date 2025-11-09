import nltk
from nltk.tokenize import word_tokenize
from tkinter import Tk, Label, Button, Entry, StringVar

nltk.download('punkt_tab')

# Crie a janela
janela = Tk()

# Crie a variável para a resposta
resposta = StringVar()

# Função para processar a entrada
def processar_entrada():
    entrada = entrada_usuario.get()
    tokens = word_tokenize(entrada)
    # Faça algo com os tokens...
    resposta.set("Olá! Eu entendi que você disse: " + entrada)

# Crie a interface
Label(janela, text="Digite algo:").pack()
entrada_usuario = Entry(janela)
entrada_usuario.pack()
Button(janela, text="Enviar", command=processar_entrada).pack()
Label(janela, textvariable=resposta).pack()

# Inicie a janela
janela.mainloop()