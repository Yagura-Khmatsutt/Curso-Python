num1 = int(input('Escreva um número inteiro:'))
num2 = int(input('Escreva outro número inteiro:'))
print('Os valores escritos são {} e {}'.format(num1, num2))

if num1 > num2:
    print('O primeiro número é MAIOR.')
elif num2 > num1:
    print('O segundo número é MAIOR.')
else:
    print('Os Valores são iguias.')

