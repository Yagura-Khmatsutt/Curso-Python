'''
Dentro do pacote utilidades que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.
'''
from utilidades.moedas import ex110
from utilidades import dados

p = dados.leiaMoney('Dígite um valor: ')
ex110.resumo(p, 35, 25)
