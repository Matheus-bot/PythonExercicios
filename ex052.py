# 52 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número para saber se ele é um número primo: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot +=1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes '.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

'''
numero = int(input('digite um número: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f' {c}', end='')
print(f'\n\033[mO número {numero} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO')
'''
