#Faça um programa que leia um número inteiro e mostre  na tela o  seu sucessor e seu antecessor

num = int(input('Digite um numero:'))

#Com varável:
a = num - 1
s = num + 1
print('Analisando o valor {}, seu\033[0;34m antecessor\033[m é {} e o \033[0;35msucessor\033[m é {}'.format(num, a, s))

#Sem variável:
print('Analisando o valor {}, seu\033[0;35m antecessor\033[m é {} e o\033[0;34m sucessor\033[m é {}' .format(num, (num-1), (num+1)))