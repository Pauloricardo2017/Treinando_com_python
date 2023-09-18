# Desenvolva um programa que pergunte
# a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km
# para viagens de até 200Km
# e R$0,45 para viagens mais longas.

dis = float(input('Qual a distância da viagem? '))
if dis <= 200:
    val1 = dis*0.50
    print('Voçê está preste a começar uma viagem de {}km. \nE o preço de sua passagem será de R${:.2f}'.format(dis, val1))
else:
    val2 = dis*0.45
    print('Você está preste a começar uma viagem de {}km.\nE o preço da sua passagem será de R${:.2f}'.format(dis, val2))
    
