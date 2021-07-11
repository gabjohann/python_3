# Faça um programa que leia o comprimento do cateto oposto e a do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot

catoposto = float(input('Cateto oposto: '))
catadjacente = float(input('Cateto adjacente: '))
print(hypot(catoposto, catadjacente))

'''
Solução da aula:
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa mede {:.2f}'.format(hi))
'''
