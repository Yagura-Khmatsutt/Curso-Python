print('Analise de dados')
tot18 = totH = totM = 0
while True:
    sexo = ' '
    idade = int(input('IDADE:'))

    while sexo not  in 'MF':
        sexo = str(input('Sexo [M/ F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM += 1

    res = ' '
    while res not in'SN':
        res = str(input('Quer continuar:[S/N] ')).strip().upper()[0]
    if res == 'N':
        break
print(f'Total de pessoass com mais de 18 {tot18}, homens cadastrados {totH} mulheres menores de 20 {totM}')
