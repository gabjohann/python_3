# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# ex.: Ana Maria de Souza
#   primeiro: Ana
#   último: Souza

nome = str(input('Digite seu nome completo: ')).strip()
onome = nome.split()
print('Seu primeiro nome é: {}\n'
      'Seu último nome é: {}'.format(onome[0], onome[len(onome)-1]))


# Resolução da aula

# n = str(input('Digite seu nome completo: ')).strip()
# nome = n.split()
# print('Muito prazer em te conhecer!')
# print('Seu primeiro nome é {}'.format(nome[0]))
# print('Seu último nome é {}'.format(nome[len(nome)-1]))
