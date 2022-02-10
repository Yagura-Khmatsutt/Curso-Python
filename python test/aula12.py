name = str(input('Qual o Seu Nome?'))
if name == 'Yagura':
    print('Um excelente dia, senhor {}!'.format(name))
elif name == 'Pedro' or name == 'João' or name == 'Maria':
    print('Seu nome é bem comum por aquí!')
    print('Bom dia {}' .format(name))
elif name == 'Matheus' or name == 'Yagu':
    print('Bom dia, Vocẽ tem muito serviço hoje!')
else:
    print('Bom dia, {}!'.format(name))
