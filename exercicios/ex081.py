'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
from time import sleep
valor = list()
for i in range(0, 5):
    n = int(input('Dígite um valor: '))
    if n not in valor:
        valor.append(n)
        print('Processando...')
        sleep(1)
        print('Valor guardado com sucesso!')
    else:
        print('Processando...')
        sleep(1)
        print('Valor duplicado![NÃO SALVO!]')
    r = str(input('Deseja continuar? [S/N]')).upper().strip()
    if r == 'N':
        break
print(valor)
