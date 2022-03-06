'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
valores = list()
mai = 0
men = 0
for c in range(0, 5):
    valores.append(int(input(f'Dígite um valor para posição {c} :')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]
print('-=' * 30)
print(f'Os valores dígitados são {valores}')
print(f'O maior valor é {mai} na posição', end=' ')
for i, v in enumerate(valores):
    if v == mai:
        print(f' {i}...')
print(f'O menor valor é {men}')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...')
