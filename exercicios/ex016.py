'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''
import math
print('Olá')
num = float(input('Dígite um valor:'))
print(f'O valor {num} tem como inteiro {math.trunc(num)}')
print('FIM!')
