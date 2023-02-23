# 61 - Refaça o desafio 051, lendo  o primeiro termo e a razão de uma PA,
# mostrando os 10  primeiros termos da progressão usando a estrutura while.

print('GERADOR DE PA')
print('-='* 10)
primeiro = int(input('Primeiro Termo '))
razão  = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
'''
print('-='*10)
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}', end='')
    print('.' if cont >= 10 else ' -> ', end='' )
    termo += razão
    cont += 1
print(' Fim')'''
