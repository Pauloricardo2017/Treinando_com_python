#  Faça um programa que leia um 
#ângulo qualquer e mostre na tela o valor do seno, 
#cosseno e tangente desse ângulo.


from math import radians, sin, tan, cos

ang = float(input('Digite um angulo: '))
seno = sin(radians(ang))
print('O angulo de {} tem o seno de {:.2f}'.format(ang, seno))
cosseno = cos(radians(ang))
print('O angulo de {} tem o cosseno de {:.2f}'.format(ang, cosseno))
tangente = tan(radians(ang))
print('O angulo de {} tem o Tangente de {:.2f}'.format(ang, tangente))
