# Faça um algoritmo que leia  salário e um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Qual seu salário? R$'))
aumento = salario + (salario * 0.15)
print('Seu salário é R${} e com o aumento de 15% ficará {:.2f}'.format(salario, aumento))
