# 64 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag(999)).

núm = cont = soma = 0
while núm != 999:
    núm = int(input('Digite um número [999 para parar]:'))
    if núm != 999:
        soma += núm
        cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

'''cont = n = soma = 0
while n != 999:
    n = int(input(f'{cont + 1}º Número'))
    cont += 1
    if n == 999:
        break
    soma += n
print(f'Foram digitados {cont - 1} números')
print(f'A soma dos números é {soma}')'''
