'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
 – A média da turma
– A situação (opcional)
'''


def notas(*n, sit=False):
    """"
    :param n: Uma ou mais notas.
    :param sit: Situação geral, coloque True para funcionar.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        if 4 < r['Média'] < 7:
            r['Situação'] = 'Razoavel'
        if r['Média'] <= 4:
            r['Situação'] = 'Ruin'
    return r


# main
resp = notas(9.5, 7.3, 4.5, 6, 3.6, 10, 9.8, sit=True)
print(resp)
