'''39- Faça  um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é hora de se alistar.
-Se já passou do tempo do alistamento .
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
'''
from datetime import date
atual = date.today().year
sexo  = int(input("""Qual seu sexo 
[1]Masculino 
[2]Feminino 
"""))
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
    print('Mas você não é obrigada a se alistar...')'''
from time import sleep
from datetime import date
print('='*22)
print('TESTE DE ALISTAMENTO')
print('='*22)
anonascimento = int(input('Em que ano você nasceu: '))
anoatual = date.today().year
idadeatual = anoatual - anonascimento
sexo = int(input('''Qual seu sexo:
[1]Masculino
[2]Feminino 
'''))
print('ANALISANDO...')
sleep(3)
if idadeatual < 18 and sexo == 1:
    print(f'''Você ainda vai se alistar no serviço militar... 
    você tem {idadeatual} anos ainda te falta {18 - idadeatual} anos ''')
elif idadeatual == 18 and sexo == 1:
    print('\033[0;34mEstá na hora de se alistar\033[m ')
elif idadeatual > 18 and sexo == 1:
    print(f'''\033[0;33mJa passou do tempo do alistamento\033[m...
    o prazo foi há {idadeatual-18} anos atrás''')
else:
    print('Você não é obrigada a se alistar')







