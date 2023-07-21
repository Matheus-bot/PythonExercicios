# 113 - Reescreva a função leiaInt() que fizemos no desadio 104, incluindo agora a possibilidade da digitação de
# um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[33mErro por favor digite um valor inteiro válido ...\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar nada')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro! por favor digite um valor real valido...')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu náo digitar nada')
            return 0
        else:
            return n

num1 = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número Real: ')
print(f'O numero inteiro digitado foi {num1} e o real foi {num2}')



