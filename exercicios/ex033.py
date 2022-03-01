'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

a = int(input('Qual primeiro valor: '))
b = int(input('Qual  segundo valor: '))
c = int(input('Qual terceiro valor: '))
menor = a
if b < a and b < c:
   menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'Maior é {maior}')
print(f'Menor é {menor}')
