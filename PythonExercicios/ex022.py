# Crie um programa que leia o nome completo de uma pessoa e mostre:
#   - o nome com todas as letras maiúsculas;
#   - o nome com todas minúsculas;
#   - quantas letras ao todo (sem considerar espaços);
#   - quantas letras tem o primeiro nome;

nome = str(input('Digite seu nome: ')).strip()
upper = nome.upper()
lower = nome.lower()
space = len(nome) - nome.count(' ')
splitt = len(nome.split()[0])
print('Seu nome em: \n'
      'letras maiúsculas é: {}\n'
      'letra minúsculas é: {}\n'
      'Seu nome tem {} de letras\n'
      'Seu primeiro nome tem {} letras\n'
      .format(upper, lower, space, splitt))

# Resolução da aula
# nome = str(input('Digite seu nome completo: ')).strip()
# print('Analisand seu nome...')
# print('Seu nome em maiúsculas é {}'.format(nome.upper()))
# print('Seu nome em minuúsculas é {}'.format(nome.lower))
# print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) --> forma 01
# separa = nome.split()
# print('Seu primiero nome é {} e ele tem {} letras'.format(separa[0], len(separa[0]))) --> forma 02
