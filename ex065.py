# 65 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar se ele quer ou não continuar a digitar valores


resp = 'S'
soma = quant = média = maior = menor = 0
while  resp in 'Ss':
    núm = int(input('Digite um número:'))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else :
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'. format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

'''
continuar = 'S'
cont = soma = media = maior = menor = 0
while continuar in 'Ss':
    n = int(input('Digite um número:  '))
    soma += n
    cont += 1
    if cont == 1:
       maior = menor = n
    if n > maior:
       maior = n
    elif n < menor :
       menor = n

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Acabou')
print(f'A média é {media}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')'''


