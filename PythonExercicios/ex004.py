# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa
# e mostre uma mensagem com a data formatada

print('Vamos conferir sua data de nascimento!')
day = int(input('Digite o dia: '))
month = int(input('Digite o mês: '))
year = int(input('Digite o ano: '))
print('Sua data de nascimento é: {}/{}/{}'.format(day, month, year))
