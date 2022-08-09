from modulos.layout.layout import *
from modulos.funcionalidade.scripts import *
from time import sleep
from os import system

while True:
    system("cls")
    continuar = 'S'
    cabecalho("Jogo da Forca")
    lista_opcoes(["Jogar contra outra pessoa", "Jogar contra o computador", "Instruções", "Sair"])
    try:
        opcao = int(input("Opção: "))
        while opcao < 1 or opcao > 4:
            print("ERRO! Opção Inválida. Tente Novamente...")
            opcao = int(input("Opção: "))
    except:
        print("Opa, algo deu errado amigo! Tente Novamente...")
        sleep(2)
        system('cls')
    else:
        #Jogar contra outra pessoa
        if opcao == 1:
            while 'S' in continuar:
                system("cls")
                player = {"vidas": 7, "lista_letras": [], "letras_adivinhadas": '', "letras_erradas": ''}
                palavra = str(input("Palavra a ser adivinhada: ")).strip().lower()
                resposta = separar_letras(palavra)
                player['lista_letras'] = escrever_letra(player["letras_adivinhadas"], resposta)
                system("cls")
                
                while player["vidas"] > 0 and player["lista_letras"] != resposta and resposta is not None:
                    system("cls")
                    mostra_letra_errada(player["letras_erradas"])
                    mostra_letras(player["lista_letras"])
                    try:
                        letra_jogador = str(input("\nLetra: ")).strip().lower()[0]
                    except:
                        print("Algo deu errado! Tente Novamente...")
                        sleep(1)
                    else:
                        system("cls")
                        if letra_jogador in resposta:
                            player["letras_adivinhadas"] += letra_jogador
                        elif letra_jogador in player["letras_erradas"]:
                            print("\033[1;31mLetra já tentada\033[m")
                        else:
                            player["vidas"] -= 1
                            player["letras_erradas"] += letra_jogador

                        player['lista_letras'] = escrever_letra(player["letras_adivinhadas"], resposta)
                        mostra_letra_errada(player["letras_erradas"])
                        mostra_letras(player["lista_letras"])

                        #Jogador tenta responder
                        if player["lista_letras"] != resposta and player["vidas"] > 0:
                            tentativa = str(input("\nTentar Responder? [S/N] ")).strip().lower()[0]
                            while tentativa not in 'sn':
                                print("Opção Inválida! Tente Novamente...")
                                sleep(0.6)
                                tentativa = str(input("Tentar Responder? [S/N]")).strip().lower()[0]
                            if tentativa == "s":
                                player_resposta = str(input("Responder: ")).strip().lower()
                                if separar_letras(player_resposta) != resposta:
                                    player["vidas"] = 0
                                else:
                                    player["lista_letras"] = separar_letras(player_resposta)
                                    system("cls")
           
                #Verifica se player ganhou ou perdeu       
                ganhou_perdeu(resposta, palavra, player["lista_letras"])
                #Jogar Denovo
                continuar = str(input("Jogar Denovo? [S/N] ")).strip().upper()[0]
                while continuar not in 'SsNn':
                    print("Opção Inválida! Tente Novamente...")
                    sleep(0.6)
                    continuar = str(input("Jogar Denovo? [S/N]")).strip().upper()[0]

        #Jogar contra o computador
        elif opcao == 2:
            system("cls")
            cabecalho("Escolha o tema")
            lista_opcoes(["Filme / Animações", "Objetos", "Comida", "Jogos"])
            try:
                tema = int(input("Número do tema: "))
                while tema < 1 or tema > 4:
                    print("ERRO! Opção Inválida. Tente Novamente...")
                    tema = int(input("Tema: "))
            except:
                print("Opção INVÁLIDA! Tente novamente...")
                sleep(0.5)
                system('cls')
            else:
                system("cls")
                player = {"vidas": 7, "lista_letras": [], "letras_adivinhadas": '', "letras_erradas": ''}
                palavra_PC = escolhaPC(tema).lower().strip()
                resposta_PC = separar_letras(palavra_PC)
                player['lista_letras'] = escrever_letra(player["letras_adivinhadas"], resposta_PC)
                system("cls")
                while player["vidas"] > 0 and player["lista_letras"] != resposta_PC and resposta_PC is not None:
                    system("cls")
                    mostra_letra_errada(player["letras_erradas"])
                    mostra_letras(player["lista_letras"])
                    try:
                        letra_jogador = str(input("\nLetra: ")).strip().lower()[0]
                    except:
                        print("Algo deu errado! Tente Novamente...")
                        sleep(1)
                    else:
                        system("cls")
                        if letra_jogador in resposta_PC:
                            player["letras_adivinhadas"] += letra_jogador
                        elif letra_jogador in player["letras_erradas"]:
                            print("\033[1;31mLetra já tentada\033[m")
                        else:
                            player["vidas"] -= 1
                            player["letras_erradas"] += letra_jogador

                        player['lista_letras'] = escrever_letra(player["letras_adivinhadas"], resposta_PC)
                        mostra_letra_errada(player["letras_erradas"])
                        mostra_letras(player["lista_letras"])

                        #Jogador tenta responder
                        if player["lista_letras"] != resposta_PC and player["vidas"] > 0:
                            tentativa = str(input("\nTentar Responder? [S/N] ")).strip().lower()[0]
                            while tentativa not in 'sn':
                                print("Opção Inválida! Tente Novamente...")
                                sleep(0.6)
                                tentativa = str(input("Tentar Responder? [S/N]")).strip().lower()[0]
                            if tentativa == "s":
                                player_resposta = str(input("Responder: ")).strip().lower()
                                if separar_letras(player_resposta) != resposta_PC:
                                    player["vidas"] = 0
                                else:
                                    player["lista_letras"] = separar_letras(player_resposta)
                                    system("cls")
           
                #Verifica se player ganhou ou perdeu
                ganhou_perdeu(resposta_PC, palavra_PC, player["lista_letras"])

                #Jogar Denovo
                continuar = str(input("Jogar Denovo? [S/N] ")).strip().upper()[0]
                while continuar not in 'SsNn':
                    print("Opção Inválida! Tente Novamente...")
                    sleep(0.6)
                    continuar = str(input("Jogar Denovo? [S/N]")).strip().upper()[0]
                
            
        #Instruções
        elif opcao == 3:
            pass
        #Sair
        elif opcao == 4:
            print("Saindo...")
            sleep(1)
            break