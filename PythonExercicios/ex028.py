# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
pc = randint(0, 5)
print('Vou pensar em um número, será que você advinhar!?')
print('-------'*7)
user = int(input('Digite um número inteiro, entre 0 e 5: '))
if user == pc:
    print('Você venceu!')
else:
    print('Você perdeu! Eu pensei no número {} e não no {}'.format(pc, user))


# Resolução da aula

# from random import randint
# from time import sleep
# computador = randint(0, 5)
# print('-=-' * 20)
# print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
# print('-=-' * 20)
# jogador = int(input('Em aue número eu pensei? '))
# print('PROCESSANDO...')
# sleep(2) # faz com que tenha um delay de 2 segundos para mostrar a resposta
# if jogador == computador:
#     print('PARABÉNS! Você conseguiu me vencer!')
# else:
#     print('GANHEI! Eu pensei ono número {} e não no {}!'.format(computador, jogador))
