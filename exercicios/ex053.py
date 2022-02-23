print('PALINDROMO!')

frase = str(input('Escreva um fraze e teste se é um Palindromo:')).strip().upper()
palavra = frase.strip()
junto = ''.join(palavra)
print('apenas um teste {}'.format(junto))
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
    print(inverso)
