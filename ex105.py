# 105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação(opcional)

def notas(*n, sit=False):
    """
    -> função para analizar notas e situações de vários alunos.
    :param n: as notas para serem preenchidas (uma ou várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['quantidade'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit == True:
        if r['média'] >= 8:
            r['situação'] = 'Ótimo'
        elif r['média'] >= 7:
            r['situação'] = 'Boa'
        else:
            r['situação'] = 'Ruim'
    return r


# Programa principal
resp = notas(8.9, 4.8, 10, 3.9, sit=True)
print(resp)
help(notas)