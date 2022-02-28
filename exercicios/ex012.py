'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

print('Olá')
produto = float(input('valor do produto:R$'))
desconto = 5 /100
cont = (produto * desconto)
valorFinal = produto - cont
print(f'O valor do produto era de {produto:.2f} R$ e após um desconto de 5% passou a valer {valorFinal:.2f} R$.')
print('FIM!')

