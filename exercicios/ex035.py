'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

print('Olá')
a = float(input('segmento 1:'))
b = float(input('segmento 2:'))
c = float(input('segmento 3:'))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos assima podem formar um triângulo.')
else:
    print('Os segmentos assima não podem formar um triângulo.')
print('FIM!')
