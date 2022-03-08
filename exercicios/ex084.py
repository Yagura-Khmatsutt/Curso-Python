'''
Faça um programa que leia nome e peso de várias pessoasguardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

temp = []
princ = []

mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    print('=-' * 35)
    temp.append(float(input('Peso: ')))
    print('=-' * 35)
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar [S/N]:')).upper()
    if resp == 'N':
        break
print('=-' * 35)
print(f'Existem {len(princ)} pessoas')
print(f'O maior peso é {mai} Kg', end='')
for p in princ:
    if p[1] == mai:
        print(f' {p[0]}')
print(f'O menor peso é {men}', end='')
for p in princ:
    if p[1] == men:
        print(f' {p[0]}')
print('=-' * 35)
