print('Menu de opções')

num1 = int(input('Dígite um valor inteiro:'))
num2 = int(input('Digite um valor inteiro:'))
opçao = 0
while opçao != 5:
    print('''   
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos numerors
    [5]sair''')
    opçao = int(input('Qual a opção:'))
    if opçao == 1:
       soma = num1 + num2
       print('o valor é {}'.format(soma))

    elif opçao == 2:
        mult = num1 * num2
        print('O valor é {}'.format(mult))
    elif opcao == 3:

    elif opcao == 4:

    elif opcao == 5:

    else:
        print('Dígite outro número')

    print('Fim do programa')