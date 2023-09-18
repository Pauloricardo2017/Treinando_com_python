# Escreva um programa em Python que leia
# um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.



num = int(input('Digite um número: '))
print('''\n[1] Binario
[2] Octal
[3] Hexadecimal''')
opção = int (input('\nsua opção: '))
if opção == 1:
    print('{} Convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para Octal é iqual a {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('{} Convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida tente novamente...')
