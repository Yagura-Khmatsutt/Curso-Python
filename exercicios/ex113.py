'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um
número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''


def leiaInt(msg):

    while True:
        try:
            i = str(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro, dígite novamente...\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuario cancelou a operação!\033[m')
        else:
            return i


def leiaFloat(msg):
    while True:
        try:
            n = str(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro, dígite novamente...\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuario cancelou a operação!\033[m')
        else:
            return n


#MAIN
i = leiaInt('Dígite um número inteiro: ')
n = leiaFloat('Dígite um número real: ')
print(f'O número digitado inteiro é {i} e o real é {n} ')
