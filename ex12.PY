# Faça um algoritmo que leia o preço de um produto e
# mostre seu novo preço, com 5% de desconto.

pre = float(input('Qual é o preço do produto? R$:'))
des = pre - (pre*5/100)
print('O produto na promoção com 5% vai custar R$:{:.2f}'.format(des))

