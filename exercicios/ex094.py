'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
galera = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO!')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    resp = str(input('Deseja continuar [S/N]: ')).upper()[0]
    if resp == 'N':
        break
print(f'Ao todo foram {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A média de idade é {media:5.2f} anos')
print('O total de mulheres cadastradas é:', end=' ')
for m in galera:
    if pessoas['sexo'] == 'F':
        print(f'{pessoas["nome"]}')
print()
