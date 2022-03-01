'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
'''
print('Olá')
name = input('Qual a sua cidade? ').upper().strip()
print(name[:5] == 'SANTO')
print('FIM')