#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
#quais ele  foi alugado. Calcule o preço a pagar, Sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado

km = float(input('Quantos km foram percorridos ? '))
dias = int(input('Quantos dias o carro foi alugado ? '))
preco = (60 * dias) + (0.15 * km)
print('O preço a pagar é R${:.2f}'.format(preco))

