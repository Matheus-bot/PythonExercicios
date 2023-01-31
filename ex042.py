# 42 Refaça o DESAFIO  035  doa triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
# Equilátero Todos os Lados iguais
# Isósceles Dois lados iguais
# Escaleno Todos  os lados diferentes


 # Minha solução
print('-='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*20)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
triangulo = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
if r1 == r2 and r1 == r3 and r2 == r3 and triangulo == True:
    print('Os seguimentos acima PODEM FORMAR triângulo! ', end='')
    print(' Equilatero ')
elif r1 != r2 and r1 != r3 and r2 != r3 and triangulo == True:
    print('Os seguimentos acima PODEM FORMAR triângulo! ', end='')
    print(' Escaleno ')
elif r1 == r2 or r2 == r3 or r1 == r3 and triangulo == True:
    print('Pode formar Triangulo', end='')
    print('Isósceles')
elif triangulo == False:
    print('Não Pode formar triângulo')
# Outra solução:

'''r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triâgulo! ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    if r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acuma NÃO PODEM FORMAR triângulo')
'''

