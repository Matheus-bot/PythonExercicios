# 33 Faça um programa que leia três números e mostre qual é o maior e qual  é o menor

'''n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))
n3 = int(input('Digite o terceiro número'))

if n1 > n2 and n1 > n3:
    print('O maior é {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior é {}'.format(n2))
elif n3 > n1 and n3 > n2:
    print('O maior é {}'.format(n3))'''

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
