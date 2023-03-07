# 77 - Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Arvore', 'Borracha',
            'Casa', 'Coroa',
            'Dado', 'Escola',
            'Forca', 'Fisicamente',
            'Gato', 'Hibrido'
            )

for item in palavras:
    print(f'\nNa palavra {item.upper()} temos ', end='')
    for letras in item:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')