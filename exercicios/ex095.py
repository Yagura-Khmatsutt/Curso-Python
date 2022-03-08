'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome: '))
totPart = int(input(f'Partidas do {jogador["Nome"]}: '))
for c in range(0, totPart):
    partidas.append(int(input(f'Quantos gols na partida {c + 1}: ')))
print('=' * 30)
jogador['total'] = sum(partidas)
print(jogador)
print('=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v} ')
print('=' * 30)
print(f'O jogador {jogador["Nome"]} fez o total de {jogador["total"]} gols em {len(partidas)} partidas.')
