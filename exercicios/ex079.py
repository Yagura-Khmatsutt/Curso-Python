'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
from time import sleep
valor = list()

while True:
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
print('=' * 45)
valor.sort()
print(f'Os valores são {valor}')
