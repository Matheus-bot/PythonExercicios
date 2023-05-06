# 84 - Faça um programa que leia o nome e peso de várias pessoas guardando tudo em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.

princ = list()
temp = list()
mai = men = 0
while True :
    temp.append(str(input('Qual seu nome? ')))
    temp.append(float(input('Qual seu peso ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()


    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print(f'Ao todo temos {len(princ)} pessoas cadastradas')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()





















