# 81 - Crie um programa que vai ler vários números e colocar em uma lista. depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista

lista = []
continuar = 'S'
while continuar == 'S':
    n = lista.append(int(input('Digite um valor: ')))

    continuar = str(input('Quer continuar? [S/N]')).upper()

    if continuar == 'N':
        break

print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente: {lista} ')
if 5 in lista:
    print('Achei o número 5 na lista')
else:
    print('Não achei o número 5 na lista')



