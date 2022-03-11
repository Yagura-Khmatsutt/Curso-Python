'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de
um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def área(larg, compr):
    a = larg * compr
    print(f'As medidas {l} de largura e {c} de comprimento resultam em:')
    print(f'{a} m²')
print('-' * 30)
print('COMTROLE DE TERRENOS')
l = float(input('Largura: '))
c = float(input('Comprimento: '))
área(l, c)
