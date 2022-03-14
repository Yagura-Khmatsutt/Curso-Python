'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um
número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''
def leiaInt(msg):
    itsOk = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            itsOk = True
        else:
            print('\033[0;31mErro, dígite novamente...\033[m')
        if itsOk:
            break
    return valor


n = leiaInt('Dígite um número inteiro: ')
print(f'O número digitado é {n}')
