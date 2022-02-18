from random import randint
print('{:=^50}'.format(' JO KEN PO '))

itens = ('Papel', 'Pedra', 'Tesoura')
computador = randint(0, 2)
print("""Escolha suas opções
[0] PAPEL
[1] PEDRA
[2]TESOURA""")
escolha = int(input('Qual a sua escolha?'))

print('O jogador jogou {}'.format(escolha))
print('O computador jogou {}'.format(computador))
