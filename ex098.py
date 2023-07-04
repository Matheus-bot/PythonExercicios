# 98 - Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo e realize a contagem.  Seu programa tem que realizar três contagens através da função criada:
#
# a) De 1 até 10, de 1 em 1
# b) De 9 até 0, de 2 em 2
# c) Uma contagem personalizada.
from time import sleep


def contagem(ini, fim, passo):
    c = 0
    print('-='* 20 )
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(ini, fim):
        print(f' {c}', end='')
        sleep(0.5)
    print(' Fim!')
    print('-='* 20)


#Programa principal
contagem(1, 11, 1)
