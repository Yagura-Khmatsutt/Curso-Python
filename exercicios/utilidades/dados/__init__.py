def leiaMoney(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print('valor  invalido!')
        else:
            valido = True
            return float(entrada)



