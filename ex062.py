# 62 - Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa ecerra quando ele disser que quer mostrar 0 termos.

print('GERADOR DE PA')
print('-='* 10)
primeiro = int(input('Primeiro Termo '))
razão  = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total :
        print('{} -> '.format(termo), end='')
        termo  += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print(f'Progressão finalizada com {total} termos mostrados. ')

