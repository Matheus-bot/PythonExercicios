#41 A confederação Nacional de Natação  precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua  categoria, de acordo com a idade:
'''Até 9 anos : Mirim
Até 14 anos : Infantil
Até 19 anos: Junior
Até 20  anos: Sênior
Acima: Master'''

print('=-'*25)
print('BEM VINDOS A CONFEDERAÇÃO NACIONAL DE NATAÇÃO:')
print('=-'*25)
from datetime import date
from time import sleep
nasc = int(input('Qual o ano de nascimento ?'))
idade = date.today().year - nasc
print('...')
sleep(2)
if idade <= 9:
    print('Você esta na categoria Mirim ')
elif idade <= 14 :
    print('Você esta na categoria Infantil')
elif idade <= 19:
    print('Você esta na categoria Junior')
elif idade <= 25:
    print('Você está na categoria Sênior')
else:
    print('Você está na categoria Master')
print('Sua idade é {} anos'.format(idade))

