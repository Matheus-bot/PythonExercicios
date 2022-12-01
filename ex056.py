# 56 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa. Mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

'''
contidade = 0
for c in range(1, 5):
    nome = str(input('Qual seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = str(input('[1] Masculino [2] Feminino]'))
    contidade += idade
    media = contidade / 4
    mais
    if
    if sexo == 1:
       print('A idade do homem mais velho é {}'.format(idade))
print(contidade)
print(media)
'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 +=1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homen mais velho tem {} anos e se chama {} '.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))


















