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
    print(f'{num} Convertido para BINÁRIO é igual a \033[0;34m{bin(num)[2:]}\033[m')
elif opção == 2:
    print(f'{num} Convertido para OCTAL é igual a \033[0;35m{oct(num)[2:]}\033[m')
elif opção == 3:
    print(f'{num} Convertido para HEXADECIMAL é igual a \033[0;31m{hex(num)[2:]}\033[m')
else:
    print('Opção INVÁLIDA. Tente novamente.')

'''

num = int(input('Digite um número inteiro: '))
escolha = int(input("""Qual a base de conversão? 
[1] Binário 
[2] Octal
[3] Hexadecimal 
"""))
if escolha == 1:
    print(f'Em binário é {bin(escolha)}')
elif escolha == 2:
    print(f'{escolha} em Octal é {oct(escolha)}')
elif escolha == 3:
    print(f'{escolha} em Hexadecimal é {hex(escolha)}')


'''
