tupla = ('Lanches', 'Pizza', 'Coca', 'Pudim', 'Sorvete')
for comida in tupla:
    print(f'Eu comi {comida}')
print('-' * 20)
for c in range(0, len(tupla)):
    print(f'Eu comi {tupla[c]} na posição {c}')
print('-' * 20)
for pos, com in  enumerate(tupla):
    print(f'Eu comi {com} na posição {pos}')
print('Estou satisfeito')
print('-' * 20)
print(sorted(tupla))

a = (2, 5, 6, 9)
b = (2, 5, 9, 7, 65, 4)
c = a + b
d = b + a
print(a, b)
print(c, d)

