# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

num = int(input('Digite um número inteiro: '))
ant = num - 1
suc = num + 1
print('O sucessor de {} é {} e seu antecessor é {}'.format(num, suc, ant))

# Resolução com somente uma variável:
# print('O sucessor de {} é {} e seu antecessor é {}'.format(num, (num+1), (num-1)))
