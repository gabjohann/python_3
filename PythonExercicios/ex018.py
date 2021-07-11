# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.

from math import radians, sin, cos, tan

angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo {}°, possui seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo, seno, cosseno, tangente))
