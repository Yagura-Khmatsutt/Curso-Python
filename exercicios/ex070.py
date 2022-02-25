print('Estatisticas de Produtos')
'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
cont = valor = total = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    resp = ' '
    cont += 1
    total += preço
    if preço >= 1000:
        valor += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto


    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Você comprou {cont} produtos e custara no total de R$ {total}.')
print(f'Vocẽ comprou {valor} produtos assima de R$1000.00')
print(f'O produto mais barato foi {barato} e custou {menor}')
