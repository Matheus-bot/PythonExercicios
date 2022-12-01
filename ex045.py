#45 Crie um programa que faça o computador jogar Jokenpô  com você

import random
from time import sleep
print('..'*12)
sleep(1)
print('Vamos Jogar Jokenpô???')
sleep(1)
print('..'*12)
sleep(1)
print('Escolha uma das opções:')
escolher = int(input('[1]Pedra\n[2]Papel\n[3]Tesoura\n'))
print('Jo')
sleep(1)
print('ken')
sleep(1)
print('pô')
sleep(1)
escolha = [1, 2, 3]
jokenpo = random.choice(escolha)
if escolher == escolha:
    print('Iguais Ninguém ganhou')
elif escolher == 1 and jokenpo == 2:
    print('O computador Venceu ele escolheu Papel e você escolheu Pedra ')
elif escolher == 2 and jokenpo == 3:
    print('O computador venceu, ele escolheu Tesoura e você escolheu Papel ')
elif escolher == 3 and jokenpo == 1:
    print('O computador venceu, ele escolheu Pedra e você escolheu Tesoura ')
elif jokenpo == 1 and escolher == 2:
    print('Você venceu, o computador escolheu Pedra e você escolheu Papel ')
elif jokenpo == 2 and escolher == 3:
    print('Você venceu, o computador escolheu Papel e você escolheu Tesoura ')
elif jokenpo == 3 and escolher == 1:
    print('Você veceu, o computador escolheu Tesoura e você escolheu Pedra ')
else:
    print('Empatou você escolheu {} e  o computador escolheu {}'.format(escolher, jokenpo))



