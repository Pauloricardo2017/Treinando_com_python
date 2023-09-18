# Faça um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações
# possiveis sobre ele.

nome = input('Digite algo: ')
print ('O tipo primitivo desse valor é ',type (nome))
print('Só tem espaços?', nome.isnumeric())
print('É um número?', nome.isnumeric())
print('É alfabético', nome.isalpha())
print('É alfanumérico?', nome.isalnum())
print('Está em maiúscula?', nome.isupper())
print('Está em minúscula?', nome.islower())
print('Está capitalizada?', nome.istitle())

