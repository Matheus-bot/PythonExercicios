# 54 - Crie um programa que leia  o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores (21 anos)

from datetime import date
pessoas = 0
menores = 0
maiores = 0
for c in range(0, 7):
    anonascimento = int(input('ano de nascimento da {}ª Pessoa?'.format(pessoas +1)))
    p = date.today().year -anonascimento
    if p <= 21:
        menores += 1
    else:
        maiores += 1
    pessoas += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maiores))
print('E também tivemos {} pessoas menores de idade '.format(menores))
