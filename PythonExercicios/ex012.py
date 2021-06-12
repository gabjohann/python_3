# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Qual o preço do produto? R$'))
desconto = float(preco * 0.05)
print('O produto custa {} e com o desconto de 5%, custará {}'.format(preco, (preco - desconto)))
