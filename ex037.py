# 37- Escreva um programa que leia um número inteiro qualquer e peça par ao
# usuário escolher qual será a base de conversão :
# -1 para binário
# -2 para octal
# -3 para hexadecimal



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

'''
#Com outra formatação.
n = int(input('Digite um número:'))
base = int(input('''Qual a base de conversão?
[1] Binário
[2] Octal
[3] Hexadecimal '''))

if base == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n) [2:]}') # 0b
elif base == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}') # 0O
elif base == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}') # 0x
else:
    print('Opção inválida, Tente novamente')

    '''
