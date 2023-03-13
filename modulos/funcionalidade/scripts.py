from os import system
from random import randint

def separar_letras(pal):
    letras = []
    acentos = {'a':'áàâã', 'e':'éê', 'i':'í', 'o':'óõô', 'u':'ú', 'ç': 'ç'}
    char_especial = ['!', '@', '#', '$', '%', '¨', '&', '*', "(", ")", "_", "+", "=", '/', '.', ',', ';', '<', '>', '|']
    for l in pal:
        for k, v in acentos.items():
            if l in v:
                l = k
        if l.isalpha() or l == " " or l == "-":
            letras.append(l)
        if l in char_especial:
            l = " "
            letras.append(l)
            
    try:
        if letras[-1].isspace():
            letras.pop()
    except IndexError:
        pass
    else:
        return letras


def escrever_letra(l_adivinhada, palavra): #[c,e,s,t,o]
    letras = []
    resp_letras = {} #{"c": 0, "e": 1,"s": 2, "t": 3, "o": 4}
    try:
        for p in palavra:
            if p.isalpha():
                letras.append("_")
            elif p == " ":
                letras.append(" ")
            elif p == "-":
                letras.append("-")

        for valor in palavra:
            if valor in resp_letras:
                resp_letras[valor] = [i for i, item in enumerate(palavra) if item == valor]
            else:
                resp_letras[valor] = palavra.index(valor)
        

        for l in l_adivinhada:
            for k, v in resp_letras.items():
                cont = 0
                if l == k and palavra.count(l) == 1:
                    letras[int(v)] = l
                elif l == k and palavra.count(l) > 1:
                    quant_letras = palavra.count(l)
                    while quant_letras > 0:
                        letras[v[cont]] = l
                        cont += 1
                        quant_letras -= 1
    except:
        return None
    else:
        return letras


def ganhou_perdeu(resp, pal, jogador):
    system("cls")
    if resp is not None: 
        if jogador == resp or jogador == pal:
            print(f"\033[1;92m\nVOCÊ VENCEU!! A palavra era {''.join(resp).title()}.\033[m")
        else:
            print(f"\033[1;31m\nVOCÊ PERDEU!! A palavra era {''.join(resp).title()}.\033[m")


def escolhaPC(tema = 0):
    lista_animacoes = []
    lista_jogos = []
    try:
        if tema == 1:
            with open("modulos/funcionalidade/pc-palavras/Animacoes.txt", "r") as arq:
                lista_animacoes = arq.readlines()
                filme_escolhido = lista_animacoes[randint(0, 90)]
        elif tema == 2:
            with open("modulos/funcionalidade/pc-palavras/Jogos.txt", "r") as arq:
                lista_jogos = arq.readlines()
                filme_escolhido = lista_jogos[randint(0, 184)]
        elif tema == 3:
            pass
        elif tema == 4:
            pass
        else:
            filme_escolhido = None
    except:
        print("Erro ao abrir o arquivo!")
    finally:
        return filme_escolhido