'''
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''
print('Olá')
temperatura = float(input('Temperatura: Cº'))
Fahrenheit = temperatura * 1.8 + 32
Kelvin = temperatura * (temperatura + 273.15)
print(f'{Fahrenheit} Fº')
print('FIM')
