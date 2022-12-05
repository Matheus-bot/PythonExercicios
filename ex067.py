# 67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

from time import sleep
cont = 0
while True:
    num = int(input('Digite um número Positivo para saber sua tabuada: '))
    print('--'*21)
    if num >= 0:
        for cont in range(0, 10):
            cont += 1
            print(f'{num} X {cont} = {num * cont}')
        print('--'*21)
    else:
        break
print('Finalizando...')
sleep(1)
print('Número negativo, Programa INTERROMPIDO.')

