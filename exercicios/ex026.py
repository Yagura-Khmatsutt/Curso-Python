'''
 Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''
print('Olá')
frase = str(input('Dígite uma frase:')).upper().strip()
print('Na frase a letra A aparece {} vezes '.format(frase.count('A')))
print('FIM')
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')))
