'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
valor = list()
par = list()
impar = list()
while True:
    valor.append(int(input('Dígite um valor: ')))
    r = str(input('Deseja continuar? [S/N]')).upper().strip()
    if r == 'N':
        break
for c, v in enumerate(valor):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('=-' * 50)
print(f'Os valores dígitados são {valor}')
print(f'Os valores ímpares são {impar}')
print(f'Os valores pares são {par}')
