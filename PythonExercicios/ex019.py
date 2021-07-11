# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevno o nome do escolihdo.

from random import choice

aluno1 = (str(input('Digite o nome de um aluno: ')))
aluno2 = (str(input('Digite o nome do outro aluno: ')))
aluno3 = (str(input('Digite o nome do outro aluno: ')))
aluno4 = (str(input('Digite o nome do outro aluno: ')))
print('O aluno sorteado foi {}'.format(choice([aluno1, aluno2, aluno3, aluno4])))

'''
from random import choice
aluno1 = (str(input('Digite o nome de um aluno: ')))
aluno2 = (str(input('Digite o nome do outro aluno: ')))
aluno3 = (str(input('Digite o nome do outro aluno: ')))
aluno4 = (str(input('Digite o nome do outro aluno: ')))
alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
'''