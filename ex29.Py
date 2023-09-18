# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem 
# dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.


vel = int(input('Qual a velocidade atual do carro? '))
if vel <= 80 :
    print('Tenha um bom dia! Dirija com segurança!!')
else:
    print('Multado voçê excedeu o limite de velocidade que é de 80km/h')
    mul =7*(vel-80)
    print('Você deverá pagor um valor de: {:.2f}'.format(mul))

