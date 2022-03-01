'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''

print('Olá')
n = str(input('Dígite seu nome:')).strip().upper()
nome = n.split()
print(f'É um prazer te conhecer {n}')
print('Seu primeiro nome é {}'.format(nome[0]))
print(('Seu ultimo nome {}').format(nome[len(nome)-1]))
print('FIM')
