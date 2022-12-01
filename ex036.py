#36- Escreva um programa para o empréstimo bancário para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

'''valor = float(input('Qual o valor da casa ? '))
salario = float(input('Qual seu salário? '))
qntanos = int(input('Em quantos anos você ira pagar?'))

porcentagem = salario * 30/100
pm = valor * qntanos
if pm > porcentagem:
    print('O emprestimo foi negado ')
else:
    print('Parabens seu emprestimo foi aprovado!!!')'''

casa = float(input('Valor da casa:R$'))
salário = float(input('Saláriodo coomprador: R$'))
anos = int(input('Quantos anos do financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end ='')
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
