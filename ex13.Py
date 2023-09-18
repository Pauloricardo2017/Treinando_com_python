# Faça um algoritimo que leia o salário de um funcionário 
#e mostre seu novo salário, com 15% de desconto.

sal = float(input('Qual seu Salário R$:'))
novo = sal+(sal*15/100)
print('Seu novo Salário com Aumento de 15%  é R$:{:.2f}'.format(novo))
