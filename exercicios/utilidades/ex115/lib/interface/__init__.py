def linha(tam=42):
    return '-' * tam


def leiaInt(msg):
    while True:
        try:
            opc = str(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro, dígite novamente...\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mErro, o usuario cancelou a operação!\033[m')
            return 0
        else:
            return opc


def head(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    head('MENU PRINCIPAL')
    i = 1
    for item in lista:
        print(f'{i} >> {item}')
        i += 1
    print(linha())
    opção = leiaInt('Sua opção é: ')
    return opção
