#24Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.

c = str(input('Qual cidade voçê nasceu? ')).strip()
print(c[:5].upper() == 'SANTO')

