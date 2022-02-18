from random import randint
from time import sleep
print('{:=^50}'.format(' JO KEN PO '))

itens = ('Papel', 'Pedra', 'Tesoura')
computador = randint(0, 2)
print("""Escolha suas opções
[0] PAPEL
[1] PEDRA
[2]TESOURA""")
escolha = int(input('Qual a sua escolha?'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.6)
print('-=' * 20)
print('Voce jogou {}'.format(itens[escolha]))
print('O computador jogou {}'.format(itens[computador]))
print('-=' * 20)

if computador == 0:
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('VOCE PERDEU!')
    elif escolha == 2:
        print(' VOCE GANHOU')
    else:
        print('jogada invalida')
elif computador == 1:
    if escolha == 0:
        print('VOCE GANHOU')
    elif escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('VOCE PERDEU')
    else:
        print('jogada invalida')
elif computador == 2:
    if escolha == 0:
        print('VOCE PERDEU')
    elif escolha == 1:
        print('VOCE GANHOU')
    elif escolha == 2:
        print('EMPATE')
    else:
        print('jogada invalida')
