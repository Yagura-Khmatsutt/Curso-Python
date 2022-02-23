print('Números primos')

numer = int(input('Dígite um número:'))
tot = 0
for cont in range(1, numer+ 1):
    if numer % cont == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[34m', end=' ')
    print('{}'.format(cont), end=' ')

print('\nO número {} foi divisivel por {} vezes.'.format(numer, tot))
if tot == 2:
    print('\033[032mO número é PRIMO')
else:
    print('\033[031mEle NÃO É PRIMO')
