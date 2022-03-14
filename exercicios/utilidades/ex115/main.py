from lib.interface import *

head('CADASTROS v1.0')

while True:
    resp = menu(['Novo cadastro', 'Verificar lista', 'Sair'])
    if resp == 1:
        print('Opção 1')
    elif resp == 2:
        print('Opção 2')
    elif resp == 3:
        print('Encerrando sistema... volte sempre!')
        break
    else:
        print('Erro!')

