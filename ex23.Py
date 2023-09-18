# Faça um programa que leia 
# um número de 0 a 9999 
#e mostre na tela cada um dos dígitos separados.

numero = int(input('Informe um número: '))
print('Analisando o número {}'.format(numero))
u = numero //1 % 10
d = numero // 10 % 10
c = numero //100 % 10
m = numero //1000 % 10
print('unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('centena: {}'.format(c))
print('Milhar: {}'.format(m))


