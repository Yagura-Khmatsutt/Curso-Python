'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''
print('Olá')
name = str(input('Seu nome:')).strip()
print('Seu nome tem siva? {}'.format('silva' in name.lower()))
print('FIM')