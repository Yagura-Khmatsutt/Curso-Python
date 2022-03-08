'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter
players = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6),}
print('=' * 30)
print('Sorteando valores')
print('=' * 30)
sleep(0.5)
raking = dict()
for c, v in players.items():
    print(f'O {c} jogou {v}')
    sleep(0.5)
raking = sorted(players.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
for i, v in enumerate(raking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
