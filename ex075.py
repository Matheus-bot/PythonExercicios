# 75 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que  posição foi digitada o primeiro  valor 3.
# c) Quais foram os números pares.


numeros = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor')),
           int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor')))

print(f'Você digitou os valores: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes', )
if 3 in numeros:
    print(f'O número 3 apareceu primeiro na {numeros.index(3)+ 1}ª posição')
else:
    print('O número 3 não apareceu em nenhuma posição')
print('Os valores pares digitados foram ', end='')

for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
'''
print('=-'* 30)
print('<<< ANALIZANDO OS NÚMEROS >>>')
print('=-'* 30)
núm = (int(input('Digite o primeiro valor ')),
       int(input('Digite o segundo valor ')),
       int(input('Digite o terceiro valor ')),
       int(input('Digite o quarto valor '))
       )
print(f'Você digitou os valores {núm}')
contagem = núm.count(9)
if contagem == 1:
    print('O valor 9 apareceu 1 vez')
else:
    print(f'O valor 9 apareceu {contagem} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu primeiro na {núm.index(3)+ 1}ª posição')
else:
    print('O valor 3 não foi encontrado... ')
print('Os valores pares são: ', end=' ')
for n in núm:
    if n % 2 == 0:
        print(f'{n}', end=' ')
'''
