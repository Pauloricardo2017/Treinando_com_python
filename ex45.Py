# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po!!!')
print('-=' * 13)
print('Computador Jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 13)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('computador vence')
    else:
        print('Jogada inválida!')

elif computador == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada inválida!')

elif computador == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Enpate')
    else:
        print('Jogada inválida!')
