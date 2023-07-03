# 96 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular(largura e comprimento) e mostre a área do terreno.

def área(l, c):
    a = l * c
    print(f'A área de um terreno de {l}X{c} é {a}m²')


# Programa principal
print('Controle de Terrenos ')
print('-' * 20)
larg = float(input('Largura: '))
comp = float(input('Comprimento: '))
área(larg, comp)