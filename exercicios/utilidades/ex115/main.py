from lib.interface import *


while True:
    resp = menu(['Novo cadastro', 'Verificar lista', 'Sair'])
    if resp == 1:
        print('Novo cadastro')
    if resp == 2:
        print('Verificar Lista')
    if resp == 3:
        print('Encerrando processo... volte sempre!')
        break
    else:
        print('Erro')

