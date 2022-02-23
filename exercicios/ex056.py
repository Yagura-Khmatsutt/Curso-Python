print('Analizador')
somaIdade = 0
mediaIdade = 0
for p in range (1,5):
    print('-----{}ª PESSOA ------'.format(p))
    nome = str(input('NOME:'))
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO [F/M]:')).strip()
    somaIdade += idade
    mediaIdade = somaIdade / 4
    totmulher20 = 0
    if p == 1 and sexo in 'Mm':
        maiorIdadedeHome = idade
        maisVelho = nome
    if sexo in 'mM' and idade > maiorIdadedeHome:
        maiorIdadedeHome = idade
        maisVelho = nome
    if sexo in 'fF' and  idade < 20:
        totmulher20 += 1
print('A média das idades é {}'.format(mediaIdade))
print('O home mais velho tem {} anos e se chama {}'.format(maiorIdadedeHome, maisVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
