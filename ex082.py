# 82 - Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas  extras que vão conter apenas os valores pares e os valores impares digitados,
# respectivamente. Ao final, mostre o conteúdo das  três listas geradas.

'''
números = []
pares = []
impares = []
while True:
    n = int(input('Digite um número'))
    números.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = str(input('Quer continuar [S/N]')).upper()
    if continuar in 'Nn':
        break
print('=-='*20)
print(f'A lista completa é: {números} ')
print(f'A lista de pares é: {pares}')
print(f'A lista de impares é: {impares}')'''

num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num} ')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')














