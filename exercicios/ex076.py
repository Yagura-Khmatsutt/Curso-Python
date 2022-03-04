'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
print('Olá')
lista = ('Caderno', 10.50,
         'Mochila', 125,
         'Pasta', 15.59,
         'Lapis', 1.75,
         'Caneta', 1.80,
         'Borracha', 1.10,
         'Livro de Python', 199.99
         )
print('-'*40)
print('TABELA DE PREÇOS')
print('-'*40)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R${lista[i]:>9.2f}')
print('-'*40)

print('FIM!')