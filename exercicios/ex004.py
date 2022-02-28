'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.'''
print('Olá')

num = input('Dígite algo pelo teclado:')

print('O tipo primitivo é ', type(num))
print('é alfanúmerico', num.isalnum())
print('é alfabetico', num.isalpha())
print('é númerico', num.isnumeric())
print('é maiusculo', num.isupper())
print('é minusculo', num.islower())
print('é digitalizado', num.isdigit())
print('É decimal', num.isdecimal())
print('FIM!')
