'''
Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
'''
import moedas

p = float(input('Dígite um valor:R$  '))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentando o preço em 25% temos {moedas.aumentar(p, 25)}')
print(f'Diminuindo o preço em 25% temos {moedas.diminuir(p, 25)}')
