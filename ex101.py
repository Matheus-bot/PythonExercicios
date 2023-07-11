# 101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicado se uma pessoa tem voto NEGADO, OPCIONAL, OBRIGATÓRIO nas eleições.
"""from datetime import date

def voto(ano_nas):
     idade = date.today().year - ano_nas
     print('=' * 20)
     print(f'A idade é {idade}')
     if idade < 16:
          print('Voto Negado! ')
     elif idade > 15 and idade < 18:
          print('Voto Opcional! ')
     elif idade > 18:
          print('Voto Obrigatório')


# Programa principal
resultado = int(input('Em que ano você nasceu? '))
voto(resultado)
"""
def voto(ano):
     from datetime import date
     atual = date.today().year
     idade = atual - ano
     if idade < 16:
          return f'Com {idade} anos: NÃO VOTA.'
     elif 16 <= idade < 18 or idade > 65:
          return f'Com {idade} anos: VOTO OPCIONAL.'
     else:
          return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))




