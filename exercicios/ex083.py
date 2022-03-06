'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expr = (str(input('Dígite a expreção: ')))
pilha = list()
for simbol in expr:
    if simbol == '(':
        pilha.append('(')
    elif simbol == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expreção é valida!')
else:
    print('Sua expreção não valida')
