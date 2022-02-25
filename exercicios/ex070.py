print('Estatisticas de Produtos')
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    