massa = float(input('Dígite seu peso: (Kg)'))
idade = float(input('Dígite sua altura:(m)'))
imc = massa / (idade ** 2)
print('Seu IMC é de {:.2f}!'.format(imc))

if imc < 18.5:
    print('Abaixo do peso!')
elif imc > 18.5 and imc < 25:
    print('Peso Ideal!')
elif imc > 25 and imc < 30:
    print('Sobrepeso')
elif imc > 30 and imc < 40:
    print('Obesidade!')
else:
    print('Obsidade morbida')