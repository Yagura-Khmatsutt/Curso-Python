from lib.interface import *
from lib.Arquivo import *
from time import sleep

file = 'Arq.txt'
if not arquivoExiste(file):
    criarArquivo(file)

while True:
    resposta = menu(['Novo cadastro', 'Verificar lista', 'Sair'])
    if resposta == '1':
        #criarNovoCadastro(file)

    if resposta == '2':
        verLista()
    if resposta == '3':
        print('\033[32mEncerrando processo...\033[m')
        sleep(2)
        print('FIM!')
        break
    if resposta > '3':
        print('\033[031mErro número invalido!\033[m')
