# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# considere U$1,00 = R$3,27

valor = float(input('Digite o valor do dinheiro: R$'))
conversao = valor / 3.27
print('R${} equivalem a aproximadamente U${:.2f}.'.format(valor, conversao))
