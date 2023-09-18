# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terçeiro número: '))
# verificando quem é o maior
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
# verificando quem é o menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior valor digitado foi:{}'.format(maior))
print('O menor valor digitado foi:{}'.format(menor))
