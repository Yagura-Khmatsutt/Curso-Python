'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
def maior(* núm):
    cont = maior = 0
    print('=-' * 40)
    print('\nAnalizando números...')
    for valor in núm:
        print(f'{valor} ', end='',flush=False)
        if valor == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
            cont += 1
    print(f'Foram imformados {cont} valores ao todo.')
    print(f'O maior valor é {maior}')


maior(20, 6, 9, 3, 6)
maior(6, 95, 23, 87, 25)
maior(3, 68, 36, 90, 28, 33)
