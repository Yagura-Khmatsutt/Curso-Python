print('Estatisticas de Produtos')
'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

while True:

    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
