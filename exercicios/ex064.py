print('Tratando varios valores')
num = cont = soma = 0
n = int(input('Dígite o número 999 para parar'))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Dígite o número 999 para parar'))
print('Você dígitou {} números e a soma é {}'.format(cont, soma))