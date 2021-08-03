# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00; calcule um aumento de 10%
# Para inferiores ou iguais, o aumento é de  15%

salario = float(input('Digite seu sálario: '))
if salario >= 1250:
    print('Seu aumento será de 10%, totalizando {}'.format(salario+(salario*0.1)))
else:
    print('Seu aumento será de 15%, totalizando {}'.format(salario+(salario*0.15)))


# Resolução da aula

# salário = float(input('Qual é o salário do funcionário? R$'))
# if salário <= 1250:
#    novo = salário + (salário * 15 / 100)
# else:
#    novo = salário + (salário * 10 / 100)
# print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salário, novo))
