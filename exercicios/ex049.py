print('Tabuada v2.0')

valorDigitado = int(input('\33[36mDígite o valor: '))

for tabuada in range(0, 101):
    mult = valorDigitado * tabuada
    print('{} X {} = {} '.format(valorDigitado, tabuada, mult))
print('FIM')
