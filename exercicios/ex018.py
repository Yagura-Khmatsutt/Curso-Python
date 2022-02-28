'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do;;
 seno, cosseno e tangente desse ângulo.
'''
import math
print('Olá')
angulo = int(input('Qual o angulo:'))
sen = math.sin(angulo)
cos = math.cos(angulo)
tg = math.tan(angulo)
print(f'O ângulo {angulo} tem o valor do seno {sen:.2f} , cosseno {cos:.2f} e a tangente {tg:.2f}.')
print('FIM!')
