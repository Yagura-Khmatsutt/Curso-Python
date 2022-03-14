'''
Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
'''
import moedas

p = float(input('Dígite um valor:R$  '))
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando o preço de {moedas.moeda(p)} em 25% temos {moedas.moeda(moedas.aumentar(p, 25))}')
print(f'Diminuindo o preço de {moedas.moeda(p)} em 25% temos {moedas.moeda(moedas.diminuir(p, 25))}')
