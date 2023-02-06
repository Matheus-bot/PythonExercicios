# 50 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas que
# forem pares. Se o valor for ímpar desconsidere-o
'''
soma = 0
for c in range(1, 7):
    n1 = int(input('Qual o {}° número? '.format(c)))

    if n1 % 2 == 0:
        soma += n1
print('A soma dos números pares é {}'.format(soma))
'''



print('='*25)
print('\033[0;34mCONTADOR DE NÚMEROS PARES\033[m')
print('='*25)
contagem = 0
for c in range(1, 7):
    num = int(input(f'\033[0;36m{c}º número: \033[m'))
    if num % 2 == 0:
        contagem += num
print('='*30)
print(f'\033[0;36mA soma de todos os numeros pares é:\033[m {contagem}')

