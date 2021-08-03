# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

vel = float(input('Digite a velocidade do carro, em km/h: '))
multa = (vel - 80) * 7
if vel >= 80.1:
    print('Você foi multado em {}! Dirija com cuidado!'.format(multa))
else:
    print('Siga dirigindo com atenção!')


# Resolução da aula

# velocidade = float(input('Qual é a velocidade atual do carro? '))
# if velocidade > 80:
#     print('MULTADO! Você excedeu o limite  permitido que é de 80 km/h')
#     multa = (velocidade - 80) * 7
#     print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
# print('Tenha um bom dia! Dirija com segurança!')
