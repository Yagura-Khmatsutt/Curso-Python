print('PALINDROMO!')

frase = str(input('Escreva um fraze e teste se é um Palindromo:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase {} é um Palindrmo'.format(junto))
else:
    print('A frase não é um palindromo!')
print(junto, inverso, end='')


