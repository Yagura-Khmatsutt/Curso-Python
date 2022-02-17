primeiraNota = float(input('Primeira Nota:'))
segundaNota = float(input('Segunda Nota:'))

soma = (primeiraNota + segundaNota) / 2
print('As notas {} e {} tem a média {}.'.format(primeiraNota, segundaNota, soma))

if soma >= 5 and soma <= 6.5:
    print('O aluno está em recuperação!')
elif soma < 4.9:
    print('O aluno está reprovado')
else:
    print('O aluno está aprovado!')