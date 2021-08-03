# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200 km e R$0,45 para viagens mais longas.

dist = float(input('Digite a distância da viagem, em km: '))
if dist <= 200:
    print('Sua viagem custará {.:2f} reais.'.format(dist*0.5))
else:
    print('Sua vigem custará {:.2f} reais.'.format(dist*0.45))


# Resolução da aula

# distância = float(input('Qual é a distância da sua viagem? '))
# print('Você está prestes a começar uma viagem de {} km'.format(distância))
# preço = distância * 0.50 if distância <= 200 else distância * 0.45
# if distância <= 200:
#     preço = distância * 0.50
# else:
#     preço = distância * 0.45
# print('E o preço da sua passagem será de R${:.2f}'.format(preço))
