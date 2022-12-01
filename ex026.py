'''26Faça um programa que leia uma frase pelo teclado e mostre :
   - Quantas vezes aparece a letra 'A'
   - Em que posição ela aparece a primeira vez.
   - Em que posição ela parece a última vez.'''

'''frase = str(input('Digite um frase: ')).strip()
vezes = frase.count('a') + frase.count('A') + frase.count('ã')
primeira = frase.find('a') + frase.find('A')
ultima = frase.rfind('a') + frase.find('A')
print('A letra "A" aparece {} vezes '.format(vezes))
print('A letra "A" aparece primeiro na {} posição'.format(primeira))
print('A letra "A" aparece a ultima vez na posição {}'.format(ultima))'''

frase = str(input('digite uma  frase')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra  A apareceu na posição {}'.format(frase.rfind('A')+1))
