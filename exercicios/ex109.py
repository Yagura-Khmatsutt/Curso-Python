'''
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''
import moedas

p = float(input('Dígite um valor:R$  '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p,  True)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
print(f'Aumentando o preço de {moedas.moeda(p)} em 25% temos {moedas.aumentar(p, 25, True)}')
print(f'Diminuindo o preço de {moedas.moeda(p)} em 25% temos {moedas.diminuir(p, 25, True)}')
