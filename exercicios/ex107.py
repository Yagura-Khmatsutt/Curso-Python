'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
from exercicios import moedas

p = float(input('Dígite um valor:R$  '))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentando o preço em 25% temos {moedas.aumentar(p, 25)}')
print(f'Diminuindo o preço em 25% temos {moedas.diminuir(p, 25)}')
