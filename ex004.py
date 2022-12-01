# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possiveis sobre ele

a = input('digite algo: ')
print('\033[0;31mO tipo primitivo é:\033[m', type(a))
print('\033[0;32mÉ Numerico:\033[m ', a.isnumeric())
print('\033[0;33mÉ Alfanumérico:\033[m ', a.isalnum())
print('\033[0;34mÉ Alfabeto:\033[m', a.isalpha())
print('\033[0;35mÉ um decimal:\033[m ', a.isdecimal())
print('\033[0;36mEstá em minúsculo:\033[m', a.islower())
print('\033[0;37mÉstá castelizado:\033[m ', a.istitle())
print('\033[0;38mÉstá em maiúsculo:\033[m', a.isupper())
