# 104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhando à função input() do Python,
# só que fazendo a validação para aceitar apenas um valor númerico. ex: n = leiaInt (Digite um n')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
            break
        else:
            print('\033[0;31mErro! Digite apenas número inteiro válido.\033[m')
    return valor


# Programa principal
n = leiaInt('Digite um número')
print(f'Você acaba de digitar o número  {n}')