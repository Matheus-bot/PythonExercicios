# 35 Desenvolva um programa que  leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.
'''Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros
dois lados e menor que a soma dos outros dois lados.
'''

print('-='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*20)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo')












