primeiroSeg = float(input('Primeiro segmento:'))
segundoSeg = float(input('Segundo segmento:'))
terceiroSeg = float(input('Terceiro segmento:'))

if primeiroSeg < segundoSeg + terceiroSeg and segundoSeg < primeiroSeg + terceiroSeg and terceiroSeg < primeiroSeg + segundoSeg:
    print('Eles  formar um triangulo:')
    if primeiroSeg == segundoSeg == terceiroSeg:
        print('EQUILATERO!')
    elif primeiroSeg != segundoSeg != terceiroSeg != primeiroSeg:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Eles não formam um triangulo!')