# Faça um programa que leia 
#a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta 
#necessária para pintá-la, 
#sabendo que cada litro de tinta, pinta uma área de 2m².

lar = float(input('Largura da parede em metros: '))
alt = float(input('Altura da parede em metros: '))
area = lar*alt
lt = area/2
print('A área da sua parede é de:{}m² e voçê precisará de {}L de tinta.'.format(area,lt))
