from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é sua jogada: '))
print('Jo')
sleep(1)
print('ken')
sleep(1)
print('po')
sleep(1)
print('-='*13)
print('O computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*13)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('JOGADA INVÁLIDA! ')
elif computador == 1:
    if jogador == 0:
        print('Compudador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('JOGADA INVÁLIDA! ')
elif computador == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('JOGADA INVÁLIDA! ')
else:
    print('Jogada invalidaa')

