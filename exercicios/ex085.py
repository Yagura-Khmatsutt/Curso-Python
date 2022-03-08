'''
Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''
núm = [[], []]

for cont in range(1, 8):
    valor = int(input(f'Dígite o {cont}º valor:'))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
núm[0].sort()
núm[1].sort()
print(f'Valores pares {núm[0]}')
print(f'Valores ímpares {núm[1]}')
