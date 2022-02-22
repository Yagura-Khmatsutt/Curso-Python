print('Números primos')

numer = int(input('Dígite um número:'))
tot = 0
for cont in range(1, numer+ 1):
    if numer % cont == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[35m', end='')

print('O número {} foi divisivel por {}.'.format(numer))