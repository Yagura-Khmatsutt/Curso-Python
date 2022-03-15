from ..interface import *

def arquivoExiste(file):
    try:
        ii = open(file, 'rt')
        ii.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(file):
    try:
        ii = open(file, 'wt+')
        ii.close()
    except:
        print('\033[33mHouve um erro!\033[m')
    else:
        print(f'Arquivo {file} criado com sucesso!')


def verLista(file):
    try:
        a = open(file, 'rt')
    except:
        print('\033[33mHouve um erro ao ler o arquivo!\033[m')
    else:
        head('PESSOAS CADASTRADAS!')
        print(a.readlines())
