# 100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somapar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores PARES sorteados pela  função anterior.
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando numeros de 1 a 10 ')
    for cont in range(0, 5):
        lista.append(randint(1, 10))


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


# Programa principal
numeros = list()
sorteia(numeros)
print(numeros)
somapar(numeros)