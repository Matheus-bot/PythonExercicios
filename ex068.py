# 68 - Faca um programa que jogue par ou impar com o computador. O jogo só sera interrompido quando o jogador PERDER
# mostrando o total de vitórias consecultivas que ele conquistou no final do jogo

from random import randint

while True:
    jogador = int(input('Digite um valor: '))
    computador  = randint(0,10)
    total = jogador + computador

    while escolha == 'PI':
        escolha = str(input('Você escolhe impar ou par ?'))
        if total% == 0:
            print('')
