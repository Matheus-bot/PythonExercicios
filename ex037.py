# 37- Escreva um programa que leia um número inteiro qualquer e peça par ao
# usuário escolher qual será a base de conversão :
# -1 para binário
# -2 para octal
# -3 para hexadecimal

'''num = int(input('Digite um número inteiro: '))
converção = int(input('[1] Binário \n[2] Octal\n[3] Hexadecimal '))'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO 
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua opção'))
if opção == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção INVÁLIDA. Tente novamente.')

