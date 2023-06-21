# 90- Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final mostre o conteúdo da estrutura na tela
"""
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno["media"] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')

"""

dados = dict()

dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]} '))

print('-='* 30)
aprovado = False
if dados['media'] > 6:
    dados['situação'] = 'Aprovado'

else:
    dados['situação'] = 'Reprovado'

for k, v in dados.items():
    print(f'{k} é igual a {v}')

























