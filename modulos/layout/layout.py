def linha():
    print("=" * 30)


def cabecalho(titulo = "Jogo"):
    print("=" * 30)
    print(f"\t{titulo}")
    print("=" * 30)


def lista_opcoes(lista = ["Undefined", "Undefined", "Undefined"]):
    copia_lista = lista.copy()
    for indice, valor in enumerate(copia_lista):
        print(f"{indice + 1} -> {valor}")
    print("=" * 30)


def desenho_inicial(pal):
    for l in pal:
        if l.isalpha():
            print("_", end=' ')
        elif l == " ":
            print("", end=' ') 
        elif l == "-":
            print("-", end=' ')


def mostra_letra_errada(lista_letras):
    for c in range(len(lista_letras)):
        if c < len(lista_letras) - 1:
            print(f"\033[1;34m{lista_letras[c]}\033[m", end='-')
        else:
            print(f"\033[1;34m{lista_letras[c]}\033[m", end='\n')