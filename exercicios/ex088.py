'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa
vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''
from random import randint
from  time import  sleep
print('-/-' * 30)
print('Sorteador de Números da Mega sena!')
lista = list()
jogos = list()
total = 1
quant = int(input('Quantos sorteios você quer:'))
while total <= quant:
    cont = 0
    while True:
        núm = randint(1, 60)
        if núm not in lista:
            lista.append(núm)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'SORTEANDO JOGOS {quant}')
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1} : {l}')
    sleep(1)
print('BOA SORTE!!!')
