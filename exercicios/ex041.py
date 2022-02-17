idade = int(input('Qual a sua Idade:'))

print('De acordo com a sua idade {} a categoria é a seguinte:'.format(idade))

if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JÚNIOR')
elif idade > 19 and idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
