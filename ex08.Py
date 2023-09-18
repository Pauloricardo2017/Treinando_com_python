# escreva um programa que leia 
#um valor em metros e o 
#exiba convertido em centimetros e milimetros.

num = float(input('Digite um valor em metros: '))
cen = num*100
mil = num*1000
print('Número em metro: {} em centimetros {:.0f}cm e milimetros {:.0f}mm'.format(num,cen,mil))
