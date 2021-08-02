# Faça um programa que leia uma frase pelo teclado e mostre:
# - quantas vezes aparece a letra 'a'
# - em que posição aparece a primeira vez
# - em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).lower().strip()
print("A letra 'a' aparece {} vezes\n"
      'Ela aparece pela primeira vez na posição : {}\n'
      'Ela aparece pela última vez na posição: {}'.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))


# Resolução da aula

# frase = str(input('Digite uma frase: ')).upper().strip()
# print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
# print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
# print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
