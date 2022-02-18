from random import randint
print('{:=^50}'.format(' JO KEN PO '))

itens = ('Papel', 'Pedra', 'Tesoura')
computador = randint(0, 2)
print("""Escolha suas opções
[0] PAPEL
[1] PEDRA
[2]TESOURA""")
escolha = int(input('Qual a sua escolha?'))

print('-=' * 20)
print('O jogador jogou {}'.format(itens[escolha]))
print('O computador jogou {}'.format(itens[computador]))
print('-=' * 20)

