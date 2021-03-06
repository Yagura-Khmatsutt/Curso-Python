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
        ii = open(file, 'rt')
    except:
        print('\033[33mHouve um erro ao ler o arquivo!\033[m')
    else:
        head('PESSOAS CADASTRADAS!')
        for l in ii:
            dado = l.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]:<10}{dado[1]:<3} anos{dado[2]:>10}')
    finally:
        ii.close()


def cadastrar(file, nome='Desconhecido', idade=0, profissão='Nula'):
    try:
        ii = open(file, 'at')
    except:
        print('\033[33mHouve um erro!\033[m')
    else:
        try:
            ii.write(f'{nome}; {idade}; {profissão}\n')
        except:
            print('\033[33mHouve um erro!\033[m')
        else:
            print(f'Novo cadastro de {nome} adicionado.')
            ii.close()



