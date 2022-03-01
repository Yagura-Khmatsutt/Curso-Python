'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = int(input('Qual o salario: R$'))

if salario <= 1250:
    novoValor = (salario * 0.15) + salario
else:
    novoValor = (salario * 0.10) + salario
print(f'O valor do salario passou a ser {novoValor} R$')
