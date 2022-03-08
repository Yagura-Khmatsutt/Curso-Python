'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome: '))
    totPart = int(input(f'Partidas do {jogador["Nome"]}: '))
    partidas.clear()
    for c in range(0, totPart):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar: [S/N]: ')).upper()[0]
        if resp in 'SN':
           break
        print('[ERRO:] Dígite S para continuar ou N para parar')
    if resp == 'N':
        break
print('-' * 40)
print('Cod', end='')
for a in jogador.keys():
    print(f'{a:<15}', end=' ')
print()
for j, l in enumerate(time):
    print(f'{j:>3}', end='')
    for i in l.values():
        print(f'{str(i):>15}', end=' ')
    print('')
print('-' * 40)
