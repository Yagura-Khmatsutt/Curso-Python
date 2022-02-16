valor = int(input('Dígite um número:'))
print('''Escolha a base para ser convertida:
[1] Binaria
[2] Octal
[3] hexadecimal''')

opcao = int(input('Sua opção:'))

if opcao == 1:
    print("O valor {} convertido para binario é {}".format(valor, bin(valor)[2:]))
elif opcao == 2:
    print("O valor {} convertido para octal é {}" .format(valor, oct(valor)[2:]))
elif opcao == 3:
    print("O valor {} convertido para Hexadecimal é {}".format(valor, hex(valor)[2:]))
else:
    print('Opção Invalida!')