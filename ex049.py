# 49 - Refaça o Desaefio 009, mostrando a tabuada de um númmero que o usuário
# escolher, só que agora utilizando um laço for

from time import sleep
print("=-"*15)
num = int(input("QUAL TABUADA VOCÊ QUER SABER?  "))
print('=-'*15)
for c in range(0, 11):
     print('{} X {} = {}'.format(num, c, num*c))
     sleep(1)
print('=-'*15)
