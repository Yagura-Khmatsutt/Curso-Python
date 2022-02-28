'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''
print('Olá')
altura = float(input('Alturra da parede:'))
comprimento = float(input('comprimento da parede:'))
totm = altura * comprimento
tinta = totm / 2
print(f'Total em {totm} m² da parede ')
print(f'Para um parde de {totm}m² vai precisar de {tinta}L tinta.')
print('FIM')
