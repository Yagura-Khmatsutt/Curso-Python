soma = cont = 0
while True:
    n = int(input('Dígite um número: [999 para parar]:'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você dígitou {cont} númros e a soma é {soma}')
