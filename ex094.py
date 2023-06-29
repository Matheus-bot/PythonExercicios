# 94 - Crie um programa que leia nome, sexo e idade de varías pessoas, guardando os dados de cada pessoa em um
# dicionário em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) A média de idade do grupo.
# c) Uma lista com todas  as mulheres.
# d) Um lista com todas a s pessoas com idade acima da média.

pessoal = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoal.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Por favor digite apenas S ou N')
    if resp == 'N':
        break

print(f'A) Ao todo temos {len(pessoal)} pessoas cadastradas ')
media = soma / len(pessoal)
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in pessoal:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in pessoal:
    if p['idade'] > media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')