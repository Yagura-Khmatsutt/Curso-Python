print('{:=^40}'.format(' LOJAS YAGURA '))
money = float(input('Dígite o valor:R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista no dinheiro
[2] à vista no cartão
[3] 2 x no cartão
[4] 3 x ou mais no cartão''')
opcao = int(input('Forma de pagamento:'))

if opcao == 1:
    calc =  money - money * 0.10
    print('O valor será:{} R$'.format(calc))
elif opcao == 2:
    calc = money - money * 0.05
    print(calc)
elif opcao == 3:
    print(money)
else:
    calc = money + money * 0.20
    print(calc)
