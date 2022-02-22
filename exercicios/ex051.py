print('Progreção Aritimetica')

primeiroTermo = int(input('Primeiro termo: '))
ultimoTermo = int(input(('Utimo termo:')))
razao = int(input('razão:'))
progArit = primeiroTermo + (ultimoTermo - 1) * razao
for progrecao in range(primeiroTermo, progArit + razao, razao):
    print('{}'.format(progrecao), end= ' -> ')