def linha():
    print("=" * 30)


def cabecalho(titulo = "Jogo"):
    linha()
    print(f"\t{titulo}")
    linha()


def lista_opcoes(lista = ["Undefined", "Undefined", "Undefined"]):
    copia_lista = lista.copy()
    for indice, valor in enumerate(copia_lista):
        print(f"{indice + 1} -> {valor}")
    linha()


def mostra_letras(pal):
    for l in pal:
        print(l.upper(), end = ' ')


def mostra_letra_errada(lista_letras):
    for c in range(len(lista_letras)):
        if c < len(lista_letras) - 1:
            print(f"\033[1;34m{lista_letras[c]}\033[m", end='-')
        else:
            print(f"\033[1;34m{lista_letras[c]}\033[m", end='\n')