'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
print('Olá!')
metros = float(input('Dígite um valor em metros: '))
km = metros / 1000
hec = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print(f'O valor {metros}')
print(f'resulta em {km} Km')
print(f'resulta em {hec} Hec')
print(f'resulta em {dam} Dam')
print(f'resulta em {dm} dm')
print(f'resulta em {cm} cm')
print(f'resulta em {mm} mm')
print('Fim')
