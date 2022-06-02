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


    #Tentativas do jogador
    desenho_inicial(resposta)
    vidas = 7
    while vidas > 0:
        letra_jogador = str(input("\n\nLetra: ")).strip().lower()[0]
        if tem_letra(letra_jogador, resposta):
            escrever_letra(letra_jogador, resposta)
        else:
            vidas -= 1

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