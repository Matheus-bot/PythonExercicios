# 58 - Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número  entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer


from random import randint
computador = randint(0, 10) # faz o computador sortear
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10. ')
print('Será que  você consegue adivinhar qual foi ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Parabéns '.format(palpites))

'''

from random import randint
print('Pensei em um número entre 0 e 5')
jogador = ''
computador = randint(0,5)
tentativas = 0
while computador != jogador:
    jogador = int(input('Em que numero eu pensei ?'))
    tentativas += 1
    if jogador == computador:
        print('Parabens você acertou')
    else:
        if jogador > computador:
            print('menos tente mais uma vez ')
        elif jogador < computador:
            print('Mais...')

print(f'Foram {tentativas} tentativas')'''

