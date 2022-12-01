# 43 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, Calcule se IMC e mostre seu status, de acordo com
# a tabela abaixo :
# Abaixo de 18.5 Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 26 até  30 Sobrepeso
# 30 até  40 Obesidade
# Acima de 40 Obesidade mórbida

peso = float(input('Qual seu peso ?'))
altura = float(input('Qual sua altura? '))
imc = peso / (altura*altura)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso ')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')
print('Seu imc é {:.2f}'.format(imc))














