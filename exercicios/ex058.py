import random
from time import sleep
print('Olá, sou seu computador, vamos jogar!')
computer = random.randint(0, 10)
sleep(2)
print('Acabei de pensar, é um número entre 0 e 10!')
print('Voce consegue acertar?')
acertou = False

while not acertou:
    
