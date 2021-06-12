# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro e tinta pinta uma área de 2m²

largura = float(input('Qual a largura da parede, em metros? '))
altura = float(input('Qual a altura da parede, em metros? '))
area = largura * altura
litros = area / 2
print('A área da sua parede é de {} m² e você precisará de {} l de tinta.'.format(area, litros))
