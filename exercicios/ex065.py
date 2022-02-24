print('Maior e menor valores!')
rsp = 'S'
soma = quantia = media = maior = menor = 0
while rsp in 'Ss':
    n = int(input('Dígite um valor:'))
    soma += n
    quantia += 1
    if quantia == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    rsp = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
media = soma / quantia
print('Vocẽ digitou {} números e a média foi {}'.format(quantia, media))
print('O maior valor foi {} e o menor foi {}!'.format(maior,menor))