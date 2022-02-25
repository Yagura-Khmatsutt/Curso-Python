n = soma = cont = 0
while n != 999:
    n = int(input('Dígite um número: [999 para parar]:'))
    soma += n
    cont += 1
print(f'Você dígitou {cont} númros e a soma é {soma}')