# 87 - Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l} {c}]'))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
print()
print('=-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
print(f'A soma dos números pares é {somapar}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]

print(f'O maior valor da segunda coluna é {mai}')

