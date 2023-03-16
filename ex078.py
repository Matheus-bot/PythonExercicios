# 78 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

'''
valores = []
maior = menor = 0
posiçãoma = posiçãome = 0
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
            posiçãoma = cont
        if valores[cont] < menor :
            menor = valores[cont]
            posiçãome = cont


print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição {posiçãoma}')
print(f'O menor valor digitado doi {menor} na posição {posiçãome}')'''

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
































