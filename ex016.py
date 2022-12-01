#Crie um programa que leia um número Real qualquer pelo  teclado e mostre na tela a sua porção inteira
#6.127 (classe math) 6
'''Primeira maneira '''
#import math
#num = float(input('Digite um número'))
#print('A porção inteira é: {}'.format(math.floor(num)))
'''Segunda Maneira'''
'''from math import trunc
num = float(input('Digite um número: '))
print('A porção inteira de {} é {}'.format(num, trunc(num)))
'''
'''Terceira maneira'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

