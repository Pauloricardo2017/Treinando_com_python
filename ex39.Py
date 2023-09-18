# Faça um programa que leia o ano de nascimento de
# um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou
# se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que
# falta ou que passou do prazo.
from datetime import date
atual = date.today().year # pegando data atual...
nasc = int(input('Ano de nacimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Voçê tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Voçê ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Voçê já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))