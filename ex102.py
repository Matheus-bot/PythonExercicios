# 102 - Crie um programa que tenha uma função chamada fatorial() que receba dois parâmetros: o primeiro que indique
# o número a calcular e o outro chamado show, que será um valor lógico (opcinal) indicando se será mostrado ou não
# na tela o processo de cáculo de fatorial

def fatorial(n, show=False):
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


print(fatorial(5, show=True))