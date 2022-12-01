#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares
#ela pode comprar. considera US$1,00 = 3,27
real = float(input('quanto dinheiro tem na carteira? R$'))
dolar = real/3.27
print('R${} equivale US${:.2f}'.format(real, dolar, dolar))
