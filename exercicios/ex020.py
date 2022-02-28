'''
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random
print('Olá')
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
print(f'Os alunos são {n1}, {n2}, {n3} e {n4}')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'O aluno escolhido foi')
print(lista)
print('FIM!')
