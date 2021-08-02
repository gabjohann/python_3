# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'Santo'

cidade = str(input('Digite o nome da cidade: ')).strip()
primeiro = cidade.upper().split()
print('SANTO' in primeiro[0])


# Resolução da Aula

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')