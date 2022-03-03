'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
print('Olá')
from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for i in n:
    print(f'{i} ',  end='')
print(f'\nO maior valor foi {max(n)}')

print(f'O menor valor foi {min(n)}')
print('FIM')