'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
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
