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

def retorna_ultimos_caracteres(qtd_caracter, palavra_recebida):
 print(palavra_recebida)
 return palavra_recebida[-qtd_caracter:]

palavra = escolhe_palavra()
print(retorna_ultimos_caracteres(2, palavra))

# if retorna_ultimos_caracteres ==