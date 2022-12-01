''''# Faça um programa que leia um número de 0  a 9999 e mostre na tela cada um dos dígitos separados
# ex: Digite o número 1834
unidade:4
dezena:3
centena:8
milhar:1'''

'''num = str(input('Digite um número de 0 a 9999: ')).split()
print('Unidade é {}'.format(num.split(num[3])))
print('Dezena  é {}'.format(num.split(num[2])))
print('Centena é {}'.format(num.split(num[1])))
print('Milhar  é {}'.format(num.split(num[0])))'''


num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número: {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))