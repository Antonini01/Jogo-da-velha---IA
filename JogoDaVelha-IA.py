# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 12:02:37 2023

@author: anton
"""
from time import sleep

tabuleiro = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

def prinTabuleiro(tabuleiro):
    print("\n" * 100)
    print(f'''
 Posições:
 -------------
 | 1 | 2 | 3 |
 -------------
 | 4 | 5 | 6 |
 -------------
 | 7 | 8 | 9 |
 -------------
 
 
 Tabuleiro:
 -------------
 | {tabuleiro[1] } | {tabuleiro[2]} | {tabuleiro[3]} |
 -------------
 | {tabuleiro[4] } | {tabuleiro[5]} | {tabuleiro[6]} |
 -------------
 | {tabuleiro[7] } | {tabuleiro[8]} | {tabuleiro[9]} |
 -------------''')

def espacoVazio(posicao):
    if tabuleiro[posicao] == ' ':
        return True
    else:
        return False

def checarEmpate():
    for chave in tabuleiro.keys():
        if tabuleiro[chave] == ' ':
            return False
    return True

def checarVitoria(letr):
    return ((tabuleiro[1] == tabuleiro[2] == tabuleiro[3] == letr) or # se isso acontecer, é True
            (tabuleiro[4] == tabuleiro[5] == tabuleiro[6] == letr) or
            (tabuleiro[7] == tabuleiro[8] == tabuleiro[9] == letr) or
            (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == letr) or
            (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == letr) or
            (tabuleiro[3] == tabuleiro[6] == tabuleiro[9] == letr) or
            (tabuleiro[1] == tabuleiro[5] == tabuleiro[9] == letr) or
            (tabuleiro[3] == tabuleiro[5] == tabuleiro[7] == letr)) # se nada acontecer, retorna False

def inserirLetra(letra, posicao):
    if espacoVazio(posicao):
        tabuleiro[posicao] = letra
        prinTabuleiro(tabuleiro)
        if checarVitoria(letra):
            print(f'{letra} venceu!')
            return True
        elif checarEmpate():
            print('Empate')
            return True
    else:
        print('Não pode inserir neste local!')
        posicao = int(input('Insira uma posição: '))
        inserirLetra(letra, posicao)
        return
    return False

def lanceJogador():
    if player == 'X':
        prinTabuleiro(tabuleiro)
    posicao = int(input(f'Insira uma posicao para "{player}": '))
    if 1 <= posicao <= 9:
        return inserirLetra(player, posicao)
    else:
        print('Insira uma número válido')
        lanceJogador()

def lanceBot():
    melhorPontuacao = -1000
    melhorLance = 0
    for chave in tabuleiro.keys():
        if espacoVazio(chave):
            tabuleiro[chave] = bot
            pontuacao = minimax(tabuleiro, 0, False)
            tabuleiro[chave] = ' ' # queremos reverter o que fizemos para poder jogar o próximo lance. jogaremos o lance mais tarde
            if pontuacao > melhorPontuacao:
                melhorPontuacao = pontuacao
                melhorLance = chave
    return inserirLetra(bot, melhorLance)

def minimax(tabuleiro, profundidade, maximizar):
    if checarVitoria(bot):
        return 1
    elif checarVitoria(player): # player
        return -1
    elif checarEmpate():
        return 0

    if maximizar: # nosso bot
        melhorPontuacao = -1000
        for chave in tabuleiro.keys():
            if espacoVazio(chave):
                tabuleiro[chave] = bot
                pontuacao = minimax(tabuleiro, 0, False)
                tabuleiro[chave] = ' ' # queremos reverter o que fizemos para poder jogar o próximo lance. jogaremos o lance mais tarde
                if pontuacao > melhorPontuacao:
                    melhorPontuacao = pontuacao
        return melhorPontuacao
    else: # bot inimigo do bot acima. Irão jogar os dois bots sozinhos
        melhorPontuacao = 1000
        for chave in tabuleiro.keys():
            if espacoVazio(chave):
                tabuleiro[chave] = player
                pontuacao = minimax(tabuleiro, 0, True) # pontuacao vai receber 1, 0 ou -1 qnd for o mais profundo na arvore
                tabuleiro[chave] = ' '
                if pontuacao < melhorPontuacao:
                    melhorPontuacao = pontuacao
        return melhorPontuacao
player = input('Quer jogar com X ou O? ').upper()
while True:
    if player == 'O':
        bot = 'X'
        sleep(1)
        if lanceBot():
            break
        if lanceJogador():
            break
    elif player == 'X':
        bot = 'O'
        sleep(1)
        if lanceJogador():
            break
        if lanceBot():
            break
