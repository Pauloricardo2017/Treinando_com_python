#Faça um programa que leia o 
#comprimento do cateto oposto 
#e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa

from math import hypot


co = float(input('Conprimento do cateto oposto :'))
ca = float(input('Comprimento do cateto adijacente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}1'.format(hi))