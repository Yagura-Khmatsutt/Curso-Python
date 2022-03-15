def arquivoExiste(file):
    try:
        ii = open(file, 'rt')
        ii.close()
    except FileNotFoundError:
        return False
    else:
        return True
