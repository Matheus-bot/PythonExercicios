# 60 - Faça um programa que leia um número  qualquer e mostre o seu fatorial.(fazer com o for e com o while)
# Ex:
# 5! = 5x4x3x2x1=120
'''
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')'''

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

