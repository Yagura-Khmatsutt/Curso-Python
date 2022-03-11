'''
: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import  sleep


def contador(i, f, p):
    if p < 0:
        p *= -1

    if p == 0:
        p = 1
    print('=-' * 40)
    print(f'Contagem de {i} até {f} com passo de {p} em {p}.')
    print('=-' * 40)

    if i < f:
        cont = 1
        while cont <= f:
            sleep(1)
            print(f'{cont} ', end='', flush=False)
            cont += p
    if i > f:
        cont = i
        while cont >= f:
            sleep(1)
            print(f'{cont} ', end='', flush=False)
            cont -= p
    print()


contador(1, 10, 1)
contador(10, 0, 2)
m = int(input('Inicio: '))
n = int(input('Fim: '))
v = int(input('Passo: '))
contador(m, n, v)
print('FIM')
