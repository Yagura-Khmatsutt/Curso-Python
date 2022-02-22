print('Somando impares multiplos de tres')
soma = 0
cont = 0
for c in range(1, 501 , 2):
    if c % 3 == 0:
        soma += c
        cont += 1

print('O valor da somatoria de todos os {} citados são {}:'.format(cont, soma))
