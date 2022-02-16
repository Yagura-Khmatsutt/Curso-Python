casa = float(input("Qual o valor da casa:"))
salario = float(input(("Qual o seu salario:")))
anos = int(input("Em quantos anos pretende pagar o imprestimo:"))
minimo = salario * 30 / 100
prestacao = casa / (anos * 12)
print('O valor da prestação é ${:.2f}' .format(prestacao))

if prestacao <= minimo:
    print('Emprestimo: APROVADO')
else:
    print('Emprestimo: NEGADO')
