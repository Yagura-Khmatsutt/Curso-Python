'''
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep
print('Olá')
print('Vamos jogar...')
print('Vou pensar em número entre 0 e 5')
num = int(input('Dígite seu palpite:'))
sleep(1)
computer = randint(0, 5)
if num != computer:
    print('Você PERDEU!')
else:
    print('Você GANHOU!')
print(f'Escolhi  esse número {computer}.')
print('FIM!')
