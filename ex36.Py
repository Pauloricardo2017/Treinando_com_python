# Pergunte o valor da casa, o salário do comprador 
# e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 
#30% do salário ou então o empréstimo será negado.


casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos deseja pagar? R$'))
prestação =  casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$:{:.2f} em {} anos.'.format (casa, anos), end=' ')
print('A prestação será de R$:{:.2f}'.format (prestação))
if prestação <= minimo:
    print('Emprestimo pode ser concedido!')
else:
    print('Emprestimo negado!')
