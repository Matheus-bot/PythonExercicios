# 57 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores  'M' ou 'F'. Caso esteje errado, peça uma
# digitação novamente até ter um valor correto.

sexo = ' '
while sexo != 'M' and sexo != 'F':
      sexo = str(input('Qual o sexo [M\F]'))
      print('Por favor digite apenas M ou F')
print('Ok Obrigado !!!')

