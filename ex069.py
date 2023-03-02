# 69 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# a) Quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.

'''
cont = homens = mulheres = 0
continuar = 'S'
while continuar in 'Ss':
    idade = int(input('Qual sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo [M]asculino [F]eminino: ')).upper().strip()[0]
    if sexo in 'Mm':
        homens +=1
    if idade >= 18:
        cont += 1
    if idade <= 20 and sexo in 'Ff':
        mulheres += 1
    continuar = str(input('Quer continuar [S|N]')).upper().strip()[0]
    if continuar in 'Nn':
        break
print(f'{cont}pessoas tem mais de 18 anos')
print(f'Foram cadastradoos {homens} homens ')
print(f'Foram cadastradas {mulheres} mulheres com menos de 20 anos')
'''


total18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')

print('Programa finalizado!!! ')












