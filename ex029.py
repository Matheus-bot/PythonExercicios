'''29 Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80kmh. mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7.00 por cada km acima do limite '''

'''v = float(input('Qual foi a velocidade do carro ?'))
multa = (v-80)*7
if v > 80:
    print('Você foi multado, Atingiu {}Km/h o valor da multa é R${:.2f}'.format(v, multa))
else:
    print("Tenha um bom dia!!! sua velocidade foi de {}Km/h".format(v))'''

velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('MULTADO ! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')




