from os import system

def separar_letras(pal):
    letras = []
    for l in pal:
        if l.isalpha() or l == " " or l == "-":
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
