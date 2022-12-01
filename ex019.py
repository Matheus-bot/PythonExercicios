#Um professor quer sortear um dos seus  quatro  alunos para apagar o quadro. Faça um  programa
#que  ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice
aluno1 = str(input('Aluno 1?'))
aluno2 = str(input('Aluno 2?'))
aluno3 = str(input('ALuno 3?'))
aluno4 = str(input('Aluno 4?'))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(lista)
print('O aluno sorteado para apagar o quadro é: {}'.format(sorteio))
