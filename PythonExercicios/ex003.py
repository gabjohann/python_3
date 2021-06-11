# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

n = input('Digite algo: ')
print('O tipo primitivo é: ', type(n))
print('É alfanumérico? ', n.isalnum())
print('É alfabético? ', n.isalpha())
print('É decimal? ', n.isdecimal())
print('É um dígito? ', n.isdigit())
print('É um identificador? ', n.isidentifier())
print('É possível ser impresso? ', n.isprintable())
print('É somente espaços? ', n.isspace())
print('Está capitalizada? ', n.istitle())
print('Está em maiúsculo? ', n.isupper())
print('Está em minúsculo? ', n.islower())
print('É um número? ', n.isnumeric())
print('Está tudo em maiúsculo? ', n.isupper())
print('É um código binário? ', n.isascii())
