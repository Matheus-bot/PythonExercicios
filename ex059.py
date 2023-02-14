# 59 - Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# # [5] sair do programa
#
# from time import sleep
# print('*'*20)
# print('----CALCULADORA----')
# print('*'*20)
# a = int(input('Digite um valor:  '))
# b = int(input('Digite outro valor:  '))
# soma = a + b
# d = 0
# while d != 5:
#     print('O que deseja fazer: ')
#     d = int(input('''
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# '''))
#     sleep(1)
#     if d == 1:
#         soma = a + b
#         print('a soma é {}'.format(soma))
#         sleep(1)
#     elif d == 2:
#         multiplicar = a * b
#         print('A multiplicação é {}'.format(multiplicar))
#         sleep(1)
#     elif d == 3 :
#         if a > b:
#             print('O maior é {}'.format(a))
#         elif b > a :
#             print('O maior é {}'.format(b))
#         else:
#             print('São iguais ')
#         sleep(1)
#     elif d == 4:
#         a = int(input('Um novo valor '))
#         b = int(input('Outro valor '))
#         sleep(1)

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar 
    [3] Maior 
    [4] Novos números 
    [5] Sair do programa''')
    opção = int(input('>>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} X {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else :
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')

    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente ')
    print('=-='*10)
print('Fim do programa! Volte sempre!')









