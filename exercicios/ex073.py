'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do Palmeiras.
'''

print('Olá')
times = ('América MG', 'Athletico PR', 'Atlético GO', 'Atlético MG', 'Avaí', 'Botafogo', 'Ceará SC', 'Corinthians',
         'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Internacional', 'Palmeiras', 'São Paulo')
print('-=' * 30)
for i in times:
    print(f'* {i}')
print('-=' * 30)
print(f'Os 5 primeiros times são{times[0:5]}')
print('-=' * 30)
print(f'Os 4 ultimos colocados são {times[12:]}')
print('-=' * 30)
print(sorted(times))
print('-=' * 30)
print(f'O palmeiras está na posição {times.index("Palmeiras")+1}ª')
print('-=' * 30)
print('FIM!')