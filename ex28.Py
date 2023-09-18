#  Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o 
# usuário tentar descobrir qual foi o número escolhido
# pelo computador. O programa deverá escrever na tela
# se o usuário venceu ou perdeu.
from time import sleep # Espera um tempo que voçê escolher
from random import randint  # faz o computador sortear um número

computador = randint(0, 5) 
print('-=-' * 20)
print('Vou pemsar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns voçê acertou...')
else:
    print('Que pena voçê errou... Tente novamente.')
    