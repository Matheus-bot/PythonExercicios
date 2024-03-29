# 102 - Crie um programa que tenha uma função chamada fatorial() que receba dois parâmetros: o primeiro que indique
# o número a calcular e o outro chamado show, que será um valor lógico (opcinal) indicando se será mostrado ou não
# na tela o processo de cáculo de fatorial

def fatorial(n, show=False):
    """
    -> Calcula o Fatorial  de um número.
    :param n: Número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um núumero n.
    """

    from time import sleep
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            sleep(0.5)
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal...
print(fatorial(5, show=True))
