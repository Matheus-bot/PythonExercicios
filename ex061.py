# 61 - Refaça o desafio 051, lendo  o primeiro termo e a razão de uma PA,
# mostrando os 10  primeiros termos da progressão usando a estrutura while.




primeiro  = int(input('Primeiro termo'))
razão = int(input('Razão'))
décimo = primeiro + (10-1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(' {} '.format(c), end='->')
print('Acabou')