# 69 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# a) Quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.

'''
contidade = masculino = feminino = 0
sexo = ''
continuar = 'Ss'
while continuar == 'Ss':
      idade = int(input('Qual sua idade ? '))
      sexo = str(input('Qual seu sexo? [M/F]'))
      continuar = str(input('Quer continuar [S/N]'))
      if idade > 18 :
         contidade += 1
         if sexo == 'Mm':
            masculino += 1
         elif sexo == 'Ff' and idade > 20:
            feminino += 1
      if continuar == 'Nn':
         break
print(f'Existem {contidade} pessoas maiores de 18 anos')
print(f'Foram cadastrados {masculino} homens')
print(f'Existem {feminino} mulheres com menos de 20 anos')'''
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












