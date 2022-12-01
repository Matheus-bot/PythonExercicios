# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule  preço da passagem,
# cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas

'''d = float(input('Digite a distância em km'))
preco1 = 0.50 * d
preco2 = 0.45 * d
if d <= 200:
    print('O Valor da viagem é de R${:.2f}'.format(preco1))
else:
    print('O valor da viagem é de R${:.2f}'.format(preco2))
'''
distância = float(input('Qual é a distância da sua viagem?'))
print('Você esta prestes a começar uma viagem de {}km'.format(distância))
'''if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45'''
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))












