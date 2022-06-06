from modulos.layout.layout import *
from modulos.funcionalidade.scripts import *
from time import sleep
from os import system

#Escolher uma opção
while True:
    system("cls")
    continuar = 'S'
    cabecalho("Jogo da Forca")
    lista_opcoes(["Jogar contra outra pessoa", "Jogar contra o computador", "Instruções", "Sair"])

    opcao = int(input("Opção: "))
    while opcao < 1 or opcao > 4:
        print("ERRO! Opção Inválida. Tente Novamente...")
        opcao = int(input("Opção: "))

    #Jogar contra outra pessoa
    if opcao == 1:
        while 'S' in continuar:
            player = {"vidas": 7, "lista_letras": [], "letras_adivinhadas": '', "letras_erradas": '', "resp_jogador": ''}
            palavra = str(input("Palavra a ser adivinhada: ")).strip().lower()
            resposta = separar_letras(palavra)
            system("cls")
            desenho_inicial(resposta)

            #Tentativas do jogador
            while player["vidas"] > 0 and player["lista_letras"] != resposta:
                tentativa = str(input("\nTentar responder? [S/N] ")).strip().upper()[0]
                #Tentar responder a palavra toda
                if tentativa == 'S':
                    player["resp_jogador"] = separar_letras(str(input("Resposta: ")).strip().lower())
                    if player["resp_jogador"] != resposta:
                        player["vidas"] = 0
                    else:
                        player["lista_letras"] = player["resp_jogador"]
                else:
                    letra_jogador = str(input("\nLetra: ")).strip().lower()[0]
                    system("cls")
                    if letra_jogador in resposta:
                        player["letras_adivinhadas"] += letra_jogador + " "  
                    elif letra_jogador in player["letras_erradas"]:
                        print("\033[1;31mLetra já tentada\033[m")
                    else:
                        player["vidas"] -= 1
                        player["letras_erradas"] += letra_jogador

                    player["lista_letras"] = escrever_letra(player["letras_adivinhadas"], resposta)
                    for c in range(0, len(player["letras_erradas"])):
                        if c < len(player["letras_erradas"]) - 1:
                            print(f"\033[1;34m{player['letras_erradas'][c]}\033[m", end='-')
                        else:
                            print(f"\033[1;34m{player['letras_erradas'][c]}\033[m", end='\n')

                    for l in player["lista_letras"]:
                        print(l, end = ' ')
                

            if player["lista_letras"] == resposta:
                print(f"\nVOCÊ VENCEU!! A palavra era {''.join(resposta)}")        
            else:
                print(f"\nVOCÊ PERDEU! A palvra era {''.join(resposta)}")                
            
            continuar = str(input("Jogar denovo? [S/N]: ")).strip().upper()[0]
            system("cls")
    
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
        break