print('fatorial')
num = int(input('Dígite um número para ver seu fatorial:'))
c = num
while c > 0:
    c -= 1
    print('{} x '.format(c), end='')
    print(' x ' if c > 1 else '=', end='')
