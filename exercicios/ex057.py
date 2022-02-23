print('Validação de dados')

sexo = str(input('Qual o sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('ERROR [Dado invalido!], Por favor degite novamente o sexo [M/F]')).strip().upper()[0]
print('Sexo {} registrado comsucesso!'.format(sexo))