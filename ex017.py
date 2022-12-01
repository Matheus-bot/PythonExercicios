'''  Faça um programa que leia o comprimento do cateto  oposto e do cateto adjacente
  de um triângulo  retângulo, calcule  e mostre o comprimento da hipotenusa'''

'''import math
cateto = float(input('Qual o comprimento do cateto oposto '))
catetoad = float(input('Qua o comprimento do cateto adjacente '))
hipotenusa = math.hypot(cateto, catetoad)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))'''

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjaente: '))
hi = (co ** 2 + ca ** 2 ) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))