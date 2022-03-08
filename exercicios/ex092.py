'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import datetime
data = dict()
data['Nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
data['Idade'] = datetime.now().year - anoNascimento
data['ctps'] = int(input('CTPS (use 0 para nenhuma): '))
print(data)
if data["ctps"] != 0:
    data['AnoContratação'] = int(input('Ano de contratação: '))
    data['Salário'] = float(input('Salário: '))
    data['aposentadoria'] = data['Idade'] + ((data['AnoContratação'] + 35) - datetime.now().year)
print('=-' * 30)
for k, v in data.items():
    print(f'{k} tem o valor {v}')
