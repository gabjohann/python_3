# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

medida = float(input('Digite o valor em metros: '))
cent = int(medida * 100)
mili = int(medida * 1000)
print('{} metros, equivalem a {} centímetros e {} milímetros'.format(medida, cent, mili))
