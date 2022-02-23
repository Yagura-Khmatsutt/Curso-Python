print('Validação de dados')

sexo = str(input('Qual o sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    print('ERROR [Dado invalido!]')
