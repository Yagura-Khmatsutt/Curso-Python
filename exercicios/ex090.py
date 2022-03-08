'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]} '))
if aluno['Média'] <= 6.5 and aluno["Média"] > 5:
    print(f'{aluno["Nome"]} está em recuperação!')
elif aluno['Média'] <= 5:
    print(f'{aluno["Nome"]} está REPROVADO!')
else:
    print(f'{aluno["Nome"]} está APROVADO')
print('FIM')
