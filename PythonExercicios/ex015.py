# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantia de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro rodou? '))
valor = (dias * 60) + (km * 0.15)
print('O valor a ser pago é de R${:.2f}'.format(valor))
