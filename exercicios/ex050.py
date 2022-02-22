print('Somando pares')
soma = 0
cont = 0
for contagem in range(1,7):
    num = int(input('Dígite o {} número:'.format(contagem)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Os valores são {} e o total é {}'.format(cont, soma))
