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


def linha(tam=42):
    return '-' * tam


def head(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    head('MENU PRINCIPAL')
    i = 1
    for item in lista:
        print(f'\033[33m{i}\033[m >> \033[34m{item}\033[m')
        i += 1
    print(linha())
    opção = leiaInt('\033[35mSua opção é:\033[m ')
    return opção
