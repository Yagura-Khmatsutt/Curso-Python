'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''


def voto(ano):
    from datetime import date
    anoAtual = date.today().year

    idade = anoAtual - ano
    if idade < 16:
       return f'A sua idade {idade} ainda não pode votar.'
    if 16 < idade < 18:
        return f'Sua idade {idade} tem como o voto OPCIONAL!'
    if 18 < idade < 65:
        return f'Sua idade {idade} tem o VOTO OBRIGATÓRIO!'
    if idade > 65:
        return f'Sua idade {idade} o voto é OPCIONAL'





anoNasc = int(input('Qual o ano de nascimeto? '))
print(voto(anoNasc))
