# 44 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
# de pagamento:
# - a Vista dinheiro/cheque: 10 % de desconto
# - a Vista no cartão: 5% de desconto
# - em até 2x no cartão : Preço  normal
# - 3x  ou mais no cartão :  20%de juros
'''
print('--' * 17)
valor = float(input(' Qual o  valor do produto? '))
print('--' * 17)
dinheiro = valor - ((10 / 100) * valor)
cartão = valor - ((5 / 100) * valor)
dcartao = valor
mcartão = valor + ((20 / 100) * valor)
print('[1] a Vista/Cheque ')
print('[2] a Vista no Cartão')
print('[3] Em até duas Vezes no Cartão')
print('[4] Três vezes ou mais no cartão')
escolha = int(input('Escolha o modo de pagamento: '))
print('--' * 17)
if escolha == 1:
    print('O valor a ser pago é R${:.2f}'.format(dinheiro))
elif escolha == 2:
    print('O valor a ser pago é R${:.2f}'.format(cartão))
elif escolha == 3:
    print('O valor a ser pago é R${:.2f}'.format(dcartao))
elif escolha == 4:
    print('O valor a ser pago é R${:.2f}'.format(mcartão))
else:
    print('Esta forma não existe!!!')
'''

print('{:=^35}'.format(' LOJAS TOPRUN '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO 
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão4''')
opção = int(input('Qual é a opção: '))

if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas: '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}X de R${:.2f} COM JUROS'.format(totalparc, parcela ))
else:
    total = preço
    print('\033[0;31mOPÇÃO INVÁLIDA de pagamento. Tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no finall. '.format(preço, total))





