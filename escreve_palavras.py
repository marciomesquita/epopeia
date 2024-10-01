import random

def escolhe_palavra():

    with open('lista_de_palavras_pt.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()

    palavra_aleatoria = random.choice(palavras)
    return palavra_aleatoria

def cria_frase(numero_de_palavras):
    frase = ""
    for i in range(numero_de_palavras):
        frase = frase + " " + escolhe_palavra()
    
    print(frase)

cria_frase(13)