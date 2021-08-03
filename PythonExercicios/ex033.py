# Faça um programa que leia três números e mostre qual é  maior e qual é o menor.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite mais um número: '))

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num2 and num3 < num2:
    menor = num3

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num2 and num3 > num2:
    maior = num3

print('O menor valor digitado foi {} e o maior valor foi {}'.format(menor, maior))


# Resolução da aula

# a = float(input('Primeiro valor: '))
# b = float(input('Segundo valor: '))
# c = float(input('Terceiro valor: '))
# menor = a
# if b < a and b < c:
#     menor = b
# if c < a and c < b:
#     menor = c
# maior = a
# if b > a and b > c:
#     maior = num2
# if c > b and c > b:
#     maior = c
# print('O menor valor digitado foi {}'.format(menor))
# print('O maior valor foi {}'.format(maior))
