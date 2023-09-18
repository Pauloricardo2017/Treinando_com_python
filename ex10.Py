# Crie um programa que leia 
#quanto dinheiro uma pessoa tem na carteira e mostre 
#quantos dólares ela pode comprar. 
#Considere 1,00=R$3,27

din = float(input('Quanto dinheiro voçê tem na carteira? R$:'))
res = din/3.27
print('Com R$:{:.2f} você pode comprar us${:.2f}'.format(din,res))
