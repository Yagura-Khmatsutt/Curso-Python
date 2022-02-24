import random
from time import sleep
print('Olá, sou seu computador, vamos jogar!')
computer = random.randint(0, 10)
sleep(2)
print('Acabei de pensar, é um número entre 0 e 10!')
print('Voce consegue acertar?')
acertou = False
palpite = 0
while not acertou:
    num = int(input('Qual é o seu palpite?'))
    palpite += 1
    if num == computer:
        acertou = True
    else:
        if num < computer:
            print('Aumente um pouco!')
        if num > computer:
            print('Diminua um pouco!')
print('Acertou! e vc gastou {} palpites'.format(palpite))

