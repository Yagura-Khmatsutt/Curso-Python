'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

print('Olá')
salarioAtual = float(input('Salario Atual:R$ '))
acrescimo = 15 / 100
novoSalario = salarioAtual + (salarioAtual * acrescimo)
print(f'O valor do novo salario após o acréscimo de 15% é {novoSalario:.2f} R$.')

print('FIM!')
