print('Maior e menor valores!')
rsp = 'S'
soma = quantia = media = 0
while rsp in 'Ss':
    n = int(input('Dígite um valor:'))
    soma += n
    quantia += 1
    rsp = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
media = soma / quantia
print('Vocẽ digitou {} números e a média foi {}'.format(quantia, media))