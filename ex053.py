# 53 - Crie um programa que leia uma frase qualquer e diga se ela é um políndromo desconsiderando os espaços
# ex- APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA BOLO, ANOTARAM A DATA DA MARATONA,

frase = str(input('Digite uma frase ')).strip().upper()
palavras = frase.split() # dividir as palavras
junto = ''.join(palavras) # juntar as palavras sem os espaços
inverso = ''
# começa com o numero de letras juntas vai ate a letra  -1 que é zero e volta  uma letra
for letra in range(len(junto) - 1, -1, -1):# da última letra até a primeira voltando a partir da última
    inverso += junto[letra]
# inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')