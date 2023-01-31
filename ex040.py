#40-Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo
#com a média atingida:
#Media abaixo de 5.0: Reprovado
#Media entre5.0 e 6.9: Recuperação
#Media 7.0 ou superior: Aprovado
from time import sleep
print('=-'*15)
print('CONSULTANDO SUA MÉDIA')
print('-='*15)
sleep(1)
n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
sleep(1)
print('=='*15)
print('ANALISANDO SUA MÉDIA...')
sleep(2)
media = (n1 + n2) / 2
if media < 5.0:
    print('\033[0;31m Reprovado!!! \033[m')
elif media == 5.0 or media < 6.9:
    print('\033[0;33m Recuperação!!! \033[m')
elif media >= 7.0:
    print('\033[0;36m Aprovado!!!\033[m')
print("A sua media é {:.1f}".format(media))
