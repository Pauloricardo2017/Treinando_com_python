# Escreva um programa que leia dois números inteiros
# e compare-os. mostrando na tela uma mensagem:

# – O primeiro valor é maior

# – O segundo valor é maior

# – Não existe valor maior, os dois são iguais

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2 :
    print('O primeiro número é maior.')
elif num1 == num2 :
    print('Não existe número maior, os dois são iguais')
else:
    print('O segundo número é maior')
