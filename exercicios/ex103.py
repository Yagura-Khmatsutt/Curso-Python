'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
 quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
 algum dado não tenha sido informado corretamente.
'''


def ficha(j='<Desconhecido>', g=0):
    print(f'O jogador {j} fez {g} gols.')



#main
nome = str(input('Nome do jogdor:'))
gols = str(input('Números de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
