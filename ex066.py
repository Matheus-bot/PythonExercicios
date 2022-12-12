# 66 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando a flag)


num = soma = cont = 0
while num != 999:
         num = int(input('Digite um número: '))
         if num != 999:
            soma += num
            cont += 1
print(f'A soma dos números digitados é {soma}')
print(f'A quantidade de números digitados foram {cont}')


# utilizando o break
'''soma = cont = 0
while True:
    num = int(input('Digite um valor(999 para parar):'))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma} ')
'''