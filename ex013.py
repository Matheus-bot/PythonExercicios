#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Qual seu salário: R$'))
aumento = salario*(15/100)
new = salario + aumento

print('O salario agora  é R${:.2f}'.format(new))

novo = salario + (salario * 15 / 100)
