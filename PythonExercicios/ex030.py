# Crie um programa que leia um número inteiro e mostra na tela se ele é par ou ímpar.

num = float(input('Digite um número: '))
resto = num % 2
if resto == 1:
    print('O número é ímpar!')
else:
    print('O número é par!')


# Resolução da aula

#  número = int(input('Me diga um número qualquer: '))
#  resultado = número % 2
#  if resultado == 0:
#     print('O número {} é PAR'.format(número))
#  else:
#     print('O número {} é ÍMPAR'.format(número))
