# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
aluno1 = str(input('Nome do aluno: '))
aluno2 = str(input('Nome do outro aluno: '))
aluno3 = str(input('Nome do outro aluno: '))
aluno4 = str(input('Nome do outro aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print('A ordem de apresentação será: {}'.format(alunos))
