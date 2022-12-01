# 50 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas que
# forem pares. Se o valor for ímpar desconsidere-o

soma = 0
for c in range(1, 7):
    n1 = int(input('Qual o {}° número? '.format(c)))
    if n1 % 2 == 0:
        soma += n1
print('A soma dos números pares é {}'.format(soma))




