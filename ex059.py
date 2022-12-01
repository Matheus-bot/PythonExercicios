# 59 - Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

from time import sleep
print('*'*20)
print('----CALCULADORA----')
print('*'*20)
a = int(input('Digite um valor:  '))
b = int(input('Digite outro valor:  '))
soma = a + b
d = 0
while d != 5:
    print('O que deseja fazer: ')
    d = int(input('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa 
'''))
    sleep(1)
    if d == 1:
        soma = a + b
        print('a soma é {}'.format(soma))
        sleep(1)
    elif d == 2:
        multiplicar = a * b
        print('A multiplicação é {}'.format(multiplicar))
        sleep(1)
    elif d == 3 :
        if a > b:
            print('O maior é {}'.format(a))
        elif b > a :
            print('O maior é {}'.format(b))
        else:
            print('São iguais ')
        sleep(1)
    elif d == 4:
        a = int(input('Um novo valor '))
        b = int(input('Outro valor '))
        sleep(1)