'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela
o processo de cálculo do fatorial.
'''


def fatorial(n, show=False):

    """"
    -> CALCULO DE FATORES <-
    :param n:  Número a ser fatorado!
    :param show: Mostra os fatores de n, False para desativar.
    :param return: retorna o resultaod
    """
    c = 1
    for i in range(n, 0, -1):
        if show:
            print(f'{i}', end='')
            if i > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        c *= i
    return c


print(fatorial(2, show=True))
help(fatorial)
