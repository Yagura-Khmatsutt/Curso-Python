from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Novo cadastro', 'Verificar lista', 'Sair'])
    if resposta == '1':
        print('Novo cadastro')
    if resposta == '2':
        print('Verificar Lista')
    if resposta == '3':
        print('\033[32mEncerrando processo...\033[m')
        sleep(2)
        print('FIM!')
        break
    if resposta > '3':
        print('\033[031mErro número invalido!\033[m')
