# 68 - Faca um programa que jogue par ou impar com o computador. O jogo só sera interrompido quando o jogador PERDER
# mostrando o total de vitórias consecultivas que ele conquistou no final do jogo

from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador  = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você escolhe impar ou par[P/I] ?')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador} o total foi de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR' )
    '''if tipo  == 'P' and total % 2 == 0:
         print('Você Venceu! ')
         v += 1
    elif tipo == 'I' and total % 2 == 1:
         print('Você Venceu! ')
         v += 1
    else:
        print('Você Perdeu: ')
        break'''
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!!')
            v += 1
        else:
            print('Você PERDEU!!!')
            break
    print('Vamos Jogar novamente ')
if v == 1:
    print(f'Você venceu {v} vez.')
else:
    print(f'Você venceu {v} vezes.')


