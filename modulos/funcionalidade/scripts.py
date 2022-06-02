from os import system

def separar_letras(pal):
    letras = []
    for l in pal:
        if l.isalpha() or l == " ":
            letras.append(l)
    return letras


def tem_letra(letra, pal):
    cont = 0
    for l in pal:
        if letra == l:
            cont += 1
    
    if cont > 0:
        return True
    else:
        return False


def escrever_letra(letra, pal):
   pass
        
