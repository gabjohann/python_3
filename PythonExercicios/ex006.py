# Crie um algoritmo que leia um número e mostre o seu dobro, o triplo e raiz quadrada

num = input('Digite um número: ')
dobro = int(num)*2
triplo = int(num)*3
raiz = float(num)**0.5
print('O dobro de {} é {}, o triplo é {} e sua raiz é {:.3f}'.format(num, dobro, triplo, raiz))

# outra forma de fazer a raiz quadrada, pow(num, (1/2))
