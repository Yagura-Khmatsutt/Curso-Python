'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao (todo sem considerar espaços).

– Quantas letras tem o primeiro nome.
'''

print('Olá')
name = str(input('Díga seu nome:'))
print(f'O seu nome em maiuscula é {name}'.upper())
print(f'O seu nome em minuscula é {name}'.lower())
print('O seu nome tem um total de {} caracteres'.format(len(name) -name.count(' ')))
print('O seu primeiro nome tem {} letras'.format(name.find(' ')))


