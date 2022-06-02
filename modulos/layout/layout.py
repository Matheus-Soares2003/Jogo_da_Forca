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



def desenhar_boneco(erros = 0):
    pass



def tela_derrota():
    pass


def tela_vitoria():
    pass