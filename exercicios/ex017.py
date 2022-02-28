'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''
import math
from math import sin, cos, hypot
print('Olá')
co = float(input('O cateto oposto vale:'))
ca = float(input('O cateto adjascente vale:'))
hipo = math.hypot(ca, co)
print(f'O valor da hipotenusa é {hipo:.1f}')
print('FIM')
