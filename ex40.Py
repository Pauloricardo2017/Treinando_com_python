# Crie um programa que leia duas notas de um aluno
# e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO


n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5 :
    print('Quem tirou entre {} e {} a média é {} e o aluno está Reprovado.'.format(n1, n2, media))
elif media <= 6.9:
    print('Quem tirou entre {} e {} a média é {} e o aluno está em Recuperação.'.format(n1, n2, media))
elif media >= 6.9:
    print('Quem tirou entre {} e {} a média é {} e o aluno está Aprovado.' .format(n1, n2, media))