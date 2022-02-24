print('Progreção aritimetica v3.0')
print('-+=' * 10)
primeiroTermo = int(input('Primeiro termo:'))
razao = int(input('Razão'))

ter = primeiroTermo
cont = 1

while cont <= 10:
    print('{} ->'.format(ter), end='')
    ter += razao
    cont += 1
print('STOP!')

plus = int(input('Quantos termos você quer mostrar?'))
