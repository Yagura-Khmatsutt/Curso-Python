'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
print('Olá')
km = int(input('Dígite a quilometragem: '))
if km <= 200:
    valor = km * 0.50
    print(f'O valor da viagem sera de {valor} R$')
else:
    valor = km * 0.45
    print(f'O valor da viagem será de {valor} R$')
print('FIM!')
