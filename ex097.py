# 97 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer  como parâmetrpo e
# mostre uma mensagem com tamanho adaptável.
#
# ex:
# escreva('Olá, Mundo!')
#
# saida:
# ~~~~~~~~~~
# Olá Mundo!
# ~~~~~~~~~~
def escreva(msg):
    tam = len(msg) + 4
    print('~'* tam)
    print(f'  {msg}')
    print('~'* tam)


#Programa principal
escreva('Ola Mundo!')
escreva('oi')
escreva('Matheus Henrique de Campos')






















