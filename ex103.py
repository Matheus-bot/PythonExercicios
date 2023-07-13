# 103 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
# jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
# dado não tenha sido informado corretamente.

def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


# Programa principal
n = str(input('Nome do jogador'))
g = str(input('Gols:'))
if g.isnumeric(): # verificar se g é numérico
    g = int(g)
else:
    g = 0
if n.strip() == '': # verifica se o nome está vazio, e passa apenas a quantidade de gols
    ficha(gols=g)
else:
    ficha(n, g)
