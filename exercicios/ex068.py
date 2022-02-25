from random import  randint
print('Jogo do par ou ímpar')
v =0
while True:
    player = int(input('Dígite um valor par ou ímpar:'))
    comp = randint(0, 10)
    tot = player + comp
    tipo = ' '
    while tipo not in'PI':
        tipo = str(input('Par ou Ímpar?')).strip().upper()[0]
    print(f'Você jogou {player} e o computador {comp}. total de {tot}')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('Voce venceu!')
            v += 1
        else:'Voce perdeu!'
        break
    print('Vamo jogar denovo?')
print(f'GAME OVER voce venceu {v} vezes')


