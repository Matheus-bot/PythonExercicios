# 79 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final serão exibidos todos os valores únicos digitados, em ordem crescente


valores = []
continuar = 'S'
while continuar in 'Ss':
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
    else:
        print('Esse valor ja está na lista... Não vou cadastrar... ')

    continuar = str(input('Quer continuar? [S/N]')).upper()

    if continuar in 'Nn':
       break
valores.sort()
print(f'Você digitou os valores {valores}')












