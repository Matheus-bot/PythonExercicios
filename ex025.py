#25 Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome.

nome = str(input('Digite é seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
