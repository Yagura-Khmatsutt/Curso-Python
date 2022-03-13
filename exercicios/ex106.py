'''
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
'''
from time import  sleep
c = ('\033[m',          # 0 sem cor
     '\033[0;30;41m',   # 1 vermelho
     '\033[0;30;42m',   # 2 verde
     '\033[0;30;43m',   # 3 amarelo
     '\033[0;30;44m',   # 4 azul
     '\033[0;30;45m',   # 5 roxo
     '\033[7;30m',      # 6 branco
     )


def ajuda(coman):
    print(f'Acessando o manual do comando \'{coman}\'', 2)
    sleep(1)
    help(coman)


def title(msg, cor=0):
    tam = len(msg) + 5
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


#Main
comand = ''
while True:
    title('Interactive helping system', 2)
    comand = str(input('Função ou Biblioteca >>> '))
    if comand.upper() == 'FIM':
        break
    else:
        ajuda(comand)
title('Até logo!', 1)
