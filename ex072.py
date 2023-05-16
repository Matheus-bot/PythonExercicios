# 72 Crie um programa que tenha uma tupla totalmente preenchida com
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20)
# e mostra-lo por extenso.
from time import sleep
cont = ('Zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'Treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte'
        )
print('='*30)
print('=== NÚMEROS POR EXTENSO ===')
print('='*30)
resp = 'S'

while True:
    while resp in 'Ss':
        num = int(input('Digite um número entre 0 e 20: '))

        if 0 <= num <= 20:
            break
        print('Tente novamente')

    print(f'Você digitou o numero {cont[num]}')
    resp = str(input('Quer continuar ? [S/N]'))
    if resp in 'Nn':
        sleep(1)
        print('========= FINALIZANDO =========')
        break










































