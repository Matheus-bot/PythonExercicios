# 72 Crie um programa que tenha uma tupla totalmente preenchida com
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20)
# e mostra-lo por extenso.


numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

continuar = 'S'
while continuar in 'SN':
    while continuar == 'S':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        num = int(input('Digite um número entre 0 e 20'))
        print(numeros[num])
        if 0 <= num <= 20:
            break

        if continuar == 'N':
            break

print('Acabou')












































