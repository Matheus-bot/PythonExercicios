#Faça um programa que leia a largura  e  a altura de uma parede em metros, calcule a sua  área e a quantidade
# de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m²

l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
area = l * a
tinta = area / 2
print('A área dessa parede é de {:.3f} metros '.format(area))
print('É necessário {} litros de tinta para pintar essa parede'.format(tinta))

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, a, area))

