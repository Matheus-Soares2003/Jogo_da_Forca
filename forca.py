from modulos.layout.layout import *
from modulos.funcionalidade.scripts import *
from time import sleep
from os import system

#Escolher uma opção
cabecalho("Jogo da Forca")
lista_opcoes(["Jogar contra outra pessoa", "Jogar contra o computador", "Instruções", "Sair"])

opcao = int(input("Opção: "))
while opcao < 1 or opcao > 4:
    print("ERRO! Opção Inválida. Tente Novamente...")
    opcao = int(input("Opção: "))

#Jogar contra outra pessoa
if opcao == 1:
    #Palavra pelo jogador
    palavra = str(input("Palavra a ser adivinhada: ")).strip().lower()
    resposta = separar_letras(palavra)
    system("cls")
    desenho_inicial(resposta)

    #Tentativas do jogador
    vidas = 7
    lista_letras = []
    letras_adivinhadas = ''
    letras_erradas = ''
    while vidas > 0 and lista_letras != resposta:
        letra_jogador = str(input("\nLetra: ")).strip().lower()[0]
        system("cls")
        if letra_jogador in resposta:
            letras_adivinhadas += letra_jogador + " "  
        else:
            vidas -= 1
            letras_erradas += letra_jogador
        

        lista_letras = escrever_letra(letras_adivinhadas, resposta)
        for c in range(0, len(letras_erradas)):
            if c < len(letras_erradas) - 1:
                print(f"{letras_erradas[c]}", end='-')
            else:
                print(f"{letras_erradas[c]}", end='\n')

        for l in lista_letras:
            print(l, end = ' ')

    system("cls")
    if lista_letras == resposta:
        print(f"VOCÊ VENCEU!! A palavra era {resposta}")        
    else:
        print(f"VOCÊ PERDEU! A palvra era {resposta}")    
        
        

#Jogar contra o computador
elif opcao == 2:
    pass

#Instruções
elif opcao == 3:
    pass

#Sair
elif opcao == 4:
    print("Saindo...")
    sleep(1)