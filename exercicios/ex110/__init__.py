def aumentar(preço=0, taxa=0, format=False):
    res = preço + (preço * taxa/100)
    return res if format is False else moeda(res)


def dobro(preço=0, format=False):
    res = preço * 2
    return res if format is False else moeda(res)


def diminuir(preço=0, taxa=0, format=False):
    res = preço - (preço * taxa/100)
    return res if format is False else moeda(res)


def metade(preço=0, format=False):
    res = preço / 2
    return res if format is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaA=0, taxaD=0):
    print('-'*40)
    print('Preço'.center(30))
    print('-'*40)
    print(f'Preço analizado {moeda(preço)}')
    print('-'*40)
    print(f'A metade é \t{metade(preço, True)}')
    print(f'O dobro é \t{dobro(preço, True)}')
    print(f'Aumentando a {taxaA} resulta em \t{aumentar(preço, taxaA, True)}')
    print(f'Diminuindo a {taxaD} resulta em \t{diminuir(preço, taxaD, True)}')
    print('-'*40)
