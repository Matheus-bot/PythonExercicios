# 49 - Refaça o Desaefio 009, mostrando a tabuada de um númmero que o usuário
# escolher, só que agora utilizando um laço for

from time import sleep
print('\033[0;35m==\033[m'* 20)
n = int(input('QUAL TABUADA VOCÊ QUER SABER? '))
print('\033[0;35m==\033[m'* 20)
for c in range(0, 11):
    print(f'\033[0;34m{n} X {c} = {n * c}\033[m')
    sleep(0.5)
