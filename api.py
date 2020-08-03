import random
# import os
# import pygame


# Note "pulos" nessa função. Você tem direito até 2 pulos nas rodadas que antecedem a questão final.
# Pressione o "p".
def rodadas(perguntas, premio=1, soma_premio=1):

    respostas_corretas = 0
    numero_pergunta = 1
    contador = 0
    pulos = 2

    while contador < 5:
        flw, rh = random.choice(list(perguntas.items()))

        # CASO SEJA A GRANDE QUESTÃO FINAL VALENDO 1 MILHÃO DE REAIS, hipoteticamente claro.
        if rh["pergunta"] == 'Qual é a empresa que está causando o maior impacto na educação do país?':
            print(
                f'\033[0;35mPergunta FINAL. Valendo {premio} MILHÃO de reais \033[m')
            pulos = 0
            print()
            print(f'\033[0;33m{rh["pergunta"]} \033[m')
        else:
            print(
                f'\033[0;35mPergunta {numero_pergunta} \033[m - Valendo {premio} MIL reais')
            print()
            print(f'\033[0;33m{rh["pergunta"]} \033[m')
            numero_pergunta += 1
            premio += soma_premio

        print()

        # CONSIDERANDO AS ALTERNATIVAS
        for rk, rv in rh['alternativas'].items():
            rk = rk.upper()
            print(f'\033[0;31m[{rk}] \033[m - {rv}')

        letra_certa = True
        while letra_certa == True:
            print()
            print(f'\033[0;31m\U0001f998: {pulos}  \033[m')
            resposta_jogador = input('Digite a sua resposta: ')
            # O jogador pode também responder com a letra maiúscula. --> .lower()
            resposta_jogador = resposta_jogador.lower()
            print()

            # TRATAMENTO DE ERRO DO USUÁRIO
            # O jogador só responde com A, B, C ou D. Maiúsculo ou minúsculo. Fugiu disso? Imprima uma mensagem de instrução e retorne.
            if resposta_jogador == 'a' or resposta_jogador == 'b' or resposta_jogador == 'c' or resposta_jogador == 'd' or resposta_jogador == 'p':
                letra_certa = False
            else:
                print('Opa, vamos lá... Digite somente: A, B, C ou D')
                letra_certa = True

        # PULOS
        if resposta_jogador == 'p' and pulos > 0:
            pulos -= 1
            respostas_corretas += 1
            resposta_jogador = resposta_jogador.lower()
            continue

        # VERIFICAÇÃO DAS RESPOSTAS
        if resposta_jogador == rh['resposta_correta']:
            print('--' * 30)
            print('\033[0;32m CERTA RESPOSTA!!! \033[m')
            print('--' * 30)
            respostas_corretas += 1

            # ESSE MÉTODO REMOVE ELEMENTOS DE POSIÇÕES ESPECÍFICAS
            perguntas.pop(flw, rh)
        else:
            print(
                '\033[0;31m QUE PENA, VOCÊ PERDEU. CONTUDO, NÃO DESANIME! DIAS DE LUTA, DIAS DE GLÓRIA!\033[m')
            print(
                f'\033[0;31m SEU PRÊMIO: {(int(premio / 3))} mil reais \033[m')
            return respostas_corretas
            break

        if respostas_corretas == 5:
            return respostas_corretas
            break

        # CASO SEJA A GRANDE QUESTÃO FINAL VALENDO 1 MILHÃO DE REAIS, hipoteticamente claro.
        if rh["pergunta"] == 'Qual é a empresa que está causando o maior impacto na educação do país?' and respostas_corretas == 1 or respostas_corretas == 0:
            return respostas_corretas

        contador += 1
        print()


"""
# Deixei uma função de stand by para possibilitar adicionar trechos musicais ao longo do game
def tocar_musica(musica):
    pygame.mixer.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()
"""


def win():
    print('\033[0;32m      VOCÊ VENCEU!!! \U0001F3C6 \U0001F3C6 \U0001F3C6  \033[m')
    print('WE ARE THE CHAMPIONS, MY FRIEND!!!')
    print()
    print()
    print('        R$1.000.000       ')


def tela_inicial():
    print('=*' * 26)
    print('\033[0;33m                \U0001F4B0 SHOW DO MILHÃO \U0001f4B0  \033[m')
    print('--' * 26)
    print('\U0001f4a1 Jovens Gênios')
    print('--' * 26)
    print('Instrução: Note que você pode pular a\nquestão. Pressione a tecla "p" se desejar.\nRegras?\n - Apenas divirta-se com tanto\n   conhecimento aleatório e variado.\n   Boa sorte, gente! \U0001F913')
    print('--' * 26)
    print()
    nome = str(input('Digite o seu nome: '))
    print(f'Olá, {nome}! \U0001F60E')
    print()
    print('\033[0;31m\U0001F913 PRIMEIRA RODADA DE PERGUNTAS \U0001F913 \033[m')


def linha_estilo():
    print('--' * 30)


def game_over():
    print('\033[0;31m    \U0001F47B GAME OVER \U0001F47B \033[m')


def chamada_rodadas(questionsX, questionsY, questionsW, THEFINAL):

    # CHAMADA DAS RODADAS SEGUINTES. SEQUÊNCIAS CONDICIONAIS; OBSERVA-SE O RESULTADO DAS 5 PERGUNTAS
    if rodadas(questionsX) == 5:
        print()
        print(
            '\033[0;31m\U0001F9D0 VAMOS LÁ! AGORA É A SEGUNDA RODADA DE PERGUNTAS \U0001F9D0\033[m')
        linha_estilo()
        if rodadas(questionsY, 10, 10) == 5:
            print()
            print(
                '\033[0;31m HUM... TÁ QUASE NO POTE DE OURO, JOVEM!\n VAMOS PARA A TERCEIRA RODADA DE PERGUNTAS \U0001F914\033[m')
            linha_estilo()
            if rodadas(questionsW, 100, 100) == 5:
                print()
                print(
                    '\033[0;34m EXCELENTE! O POTE DE OURO SIM OU CLARO? (: \n VOCÊ CHEGOU NA GRANDE QUESTÃO VALENDO 1 MILHÃO DE REAIS \033[m')
                linha_estilo()
                if rodadas(THEFINAL, 1, 1) == 1:
                    # tocar_musica('thefinal.mp3')
                    win()

                else:
                    print(
                        '\033[0;31m TENTE NOVAMENTE. VOCÊ PERDEU HOJE, MAS VAI VENCER NA PRÓXIMA! \033[m')
            else:
                game_over()
        else:
            game_over()
    else:
        game_over()
    print()
