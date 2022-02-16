from datetime import date
anoNasc = int(input('Dígite seu ano de nascimento:'))
anoAtual = date.today().year
calculo = anoAtual - anoNasc

if calculo < 18:
    print('Voce ainda não tem idade para se alistar!')
    saldo = 18 - calculo
    soma = anoAtual + saldo
    print('Faltam {} ano(s) para vc se alistar, voce só se alistara em {}'.format(saldo, soma))
elif calculo > 18:
    sobra = calculo - 18
    som = anoAtual - sobra
    print('Voce já deveria ter se ALISTADO em {}'.format(som))
else:
    print('Já está na hora de se alistar!')

