print('Progreção aritimetica v3.0')
print('-+=' * 10)
primeiroTermo = int(input('Primeiro termo:'))
razao = int(input('Razão'))

ter = primeiroTermo
cont = 1
tot = 0
plus = 10
while plus != 0:
    tot = tot + plus
    while cont <= tot:
        print('{} ->'.format(ter), end='')
        ter += razao
        cont += 1
    print('STOP!')

    plus = int(input('Quantos termos você quer mostrar?'))
print('FIM!, processo finalizado com {}  termos'.format(tot))
