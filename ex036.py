#36- Escreva um programa para o empréstimo bancário para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep
print('='*25)
print('\033[0;34m BEM VINDO AO BANCO MATT\033[m')
print('='*25)
casa = float(input('Valor da casa:R$'))
salário = float(input('Saláriodo coomprador: R$'))
anos = int(input('Quantos anos do financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('ANALISANDO...')
sleep(3)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos ', end='')
print(f'A prestação será de R${prestação:.2f}')
if prestação <= mínimo:
    print('\033[0;34mEmpréstimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[0;31mEmprestimo NEGADO!\033[m')
