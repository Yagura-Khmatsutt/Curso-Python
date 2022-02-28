'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''

import random
print('Olá')
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
print(f'Os alunos são {n1}, {n2}, {n3} e {n4}')
lista = [n1, n2, n3, n4]
escolha = random.choice(lista)
print(f'O aluno escolhido foi {escolha}')
print('FIM!')
