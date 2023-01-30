# Crie um algoritmo  que leia um número e mostre o seu dobro o seu triplo  e raiz quadrada
#num = float(input('Digite um número: '))
#dobro = num * 2
#triplo = num * 3
#raiz = num ** (1/2)
#print(' O dobro de {} é {} \n O Triplo de {} é {}\n a raiz quadrada de {} é {:.2f}'.format(num, dobro, num, triplo, num, raiz))
#pow(n(1/2))
n = int(input('Digite um número: '))
print('O dobro de {} vale \033[0;35m {}\033[m.'.format(n, (n*2)))
print('O triplo de {} vale \033[0;34m {}\033[m.\nA raiz quadrada de {} é igual a \033[0;37m{:.2f}\033[m.'.format(n, (n*3), n, pow(n, (1/2))))

