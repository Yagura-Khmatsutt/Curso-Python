from datetime import date
print('Maior Idade')
anoatual = date.today().year
totMaior = 0
totmenor = 0
for pess in range(1, 8):
    anonas = int(input('Em que ano vc nasceu: '))
    idade = anoatual - anonas
    if idade >= 18:
        totMaior += 1

    else:
       totmenor += 1
print('Ao todo tivemos {} pessoas de maior e {} pessoas de menor!'.format(totMaior, totmenor))