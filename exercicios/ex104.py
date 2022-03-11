'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
 só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
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
