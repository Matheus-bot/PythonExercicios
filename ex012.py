# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Digite o preço do produto? R$'))
desc = preco * (5/100)
novop = preco - desc
print('O desconto é de R${:.2f}'.format(desc))
print('O valor promocional é R${}'.format(novop))

