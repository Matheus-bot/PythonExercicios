# 48 -  Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que encontram
# no intervalo de 1 até 500.

a = int(input('Qual o intervalo: '))
soma = 0
cont = 0
for c in range(1, a):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
        cont += 1
print('A soma dos valores é {}'.format(soma))
print('A quantidade de valores solicitados foram {}'.format(cont))
