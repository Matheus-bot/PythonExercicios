# 28 Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para
# usuário tentar descobrir qual foi o numero escolhido pelo computador.

'''import random

ncomp = random.randint(0,5)
n = int(input('Qual numero você acha que o computador escolheu entre 0 e 5 ?'))
print(ncomp)
if ncomp == n:
    print('Parabens !!! você acertou ')
    print('Numero escolhido por você {}'.format(n))
    print('Número escolhido pelo computador {}'.format(ncomp))
else:
    print('O computador Venceu ')
    print('Número escolhido por você {}'.format(n))
    print('Número escolhido pelo computador {}'.format(ncomp))'''

from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador sortear
print('-=-' * 20)
print('Vou pensar em um número  entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))