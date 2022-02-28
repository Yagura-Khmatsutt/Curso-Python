'''
Escreva um programa;
que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
print('Olá')
dias = int(input('Quantos dias você usou o carro:'))
Km = float(input('Quantos Km você rodou:'))

valorDias = dias * 60
valorKm = Km * 0.15
print(f'O valor em dias é {valorDias:.2f} R$ e o valor em Km é {valorKm :.2f} '
      f'R$ e o total é {valorKm + valorDias:.2f} R$.')
print('FIM')
