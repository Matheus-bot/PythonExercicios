# 67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

from time import sleep
cont = 0
while True:
    num = int(input('Digite um número Positivo para saber sua tabuada: '))
    print('--'*26
          )
    if num >= 0:
        for cont in range(0, 10):
            cont += 1
            print(f'{num} X {cont} = {num * cont}')
        print('--'*26)
    else:
        break
print('Finalizando...')
sleep(1)
print('Número negativo, Programa INTERROMPIDO.')

# another solution
'''
while True:
    n =  int(input('Quer ver a tabuada de qual valor: '))
    print('_' * 30)
    if n < 0:
       break
    for c in range (1, 11):
        print(f'{n} X {c} = {n * c}')
    print('_' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre! ')'''









