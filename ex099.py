# 99 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(* num):
    cont = maior = 0
    print('-='* 20)
    print('Analizando os valores passados...')
    for v in num:
        print(f'{v} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = v
        elif v > maior:
            maior = v
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor passado é {maior}')


# Programa principal
maior(2,9, 0)
maior(0, 908, 89)
maior(0)
maior(0,76,6777)
maior(9, 999, 1232, 2)
maior(90)
maior(90, 3)