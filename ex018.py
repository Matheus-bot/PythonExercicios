#Faça um programa que leia um ângulo  qualquer e mostre na tela o valor do seno ,  cosseno e tangente desse ângulo.
''' Errado
import math
angulo = float(input('Qual o ângulo: '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('O seno de {} é {:.2f}\n O cosseno  de {} é {:.2f} \n A tangente de {} é {:.2f}'.format(angulo, seno,
angulo, cosseno, angulo, tangente))'''

from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja'))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem O COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} têm a TANGENTE de {:.2f}'.format(ângulo, tangente))