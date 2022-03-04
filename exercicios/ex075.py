'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''
print('Olá')
n = (int(input('Dígite um número:')), int(input('Dígite um número:')), int(input('Dígite um número:')),
     int(input('Dígite um número:')))
print(n)
print(f'O o número 9 apareceu {n.count(9)} vezes!')
if 3 in n:
    print(f'O número o primeiro número 3 apareceu na posição {n.index(3)+1}')
else:
    print('O valor 3 não apareceu')
print('Os vaores pares aprecem em:', end='')
for num in n:
    if num % 2 == 0:
        print(num,)
print('FIM')
