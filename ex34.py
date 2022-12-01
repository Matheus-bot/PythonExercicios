'''34 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
     Para salários superiores a 1.250.00, calcule um aumento de 10%
     Para os inferiores ou iguais, o aumento é de 15%.'''

'''salario = float(input('Qual é o seu salário? '))
aumento1 = salario * 10/100
salarios = salario + aumento1
aumento2 = salario * 15/100
salarioi = salario + aumento2
if salario > 1250:
    print('O seu novo salario é R${:.2f}'.format(salarios))
else:
    print('O seu novo salário é R${:.2f}'.format(salarioi))'''

salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salário, novo))












