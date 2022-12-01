#30 Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

n = int(input('Digite um número'))
if n%2 == 0:
    print('O número {} é Par'.format(n))
else:
    print('O número {} é Impar'.format(n))

