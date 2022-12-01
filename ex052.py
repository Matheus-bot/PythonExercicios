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
soma = 0
for c in range(0, num):
   if num % 1 == 0 and num % num == 0:
       soma += 1
       if soma < 2:
            print('É primo')
   else :
       print('Não é primo')'''

