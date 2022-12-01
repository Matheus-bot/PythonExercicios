'''39- Faça  um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é hora de se alistar.
-Se já passou do tempo do alistamento .
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
'''
from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
deveria = date.today().year - ano - 18
if idade < 18:
    print('Você ainda vai se alistar para o serviço militar !!!')
elif idade == 18:
    print('É hora de se alistar')
elif idade > 18:
    print('Ja passou do tempo do alistamento')
    print('O Prazo foi {} anos atrás'.format(deveria))
print('Sua idade é {} anos'.format(idade))'''

from datetime import date
atual = date.today().year
sexo  = int(input('''Qual seu sexo 
[1]Masculino 
[2]Feminino 
'''))
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if sexo == 1 and idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif sexo == 1 and idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif sexo == 1 and idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
else:
    print('Mas você não é obrigada a se alistar...')









