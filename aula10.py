# CONDICIONAL SIMPLES
nome = str(input('Qual é seu nome? '))
if nome == 'Lucas':
    print('Que belo nome você tem!')
print('Bom dia, {}!'.format(nome))
# só dirá que o nome é bonito, se for Lucas

# CONDICIONAL COMPOSTA
nome = str(input('Qual é seu nome? '))
if nome == 'Lucas':
    print('Que belo nome você ten!')
else:
    print('Que nome comum!')
print('Bom dia, {}!'.format(nome))
# só dirá que o nome é bonito, se for Lucas

# -------------------------------------------------------------------------------------------------------------------- #
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f'.format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')

# CONDICIONAL SIMPLIFICADA
# print ('Parabéns' if m>=6 else 'Estude mais!')