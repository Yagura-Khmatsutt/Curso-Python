'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
from datetime import date
print('Olá')
ano = int(input('Qual ano você quer verificar: Coloque 0 para verificar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Esse ano {ano} é BISSEXTO')
else:
    print(f'Esse ano {ano} não é BISSEXTO')
print('FIM')
