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
    if escolha == 1:
        print('VOCE PERDEU')
    elif escolha == 1:
        print('VOCE GANHOU')
    elif escolha == 2:
        print('EMPATE')
    else:
        print('jogada invalida')
