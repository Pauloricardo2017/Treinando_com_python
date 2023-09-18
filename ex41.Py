# A Confederação Nacional de Natação precisa
# de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria,
# de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date  # importando data
atual = date.today().year  # pegando data atual
nascimento = int(input('Ano de nacimento: '))
idade = atual - nascimento # pegando a data atual - o nacimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Atleta Mirim!')
elif idade <= 14:
    print('Atleta Infantil!')
elif idade <= 19:
    print('Atleta Júnior!')
elif idade <= 25:
    print('Atleta Senior!')
else:
    print('Atleta Master!')
