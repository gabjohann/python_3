#Importação de uma biblioteca inteira

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual é {}'.format(num, math.ceil(raiz)))

# para arredondar para cima math.ceil(raiz)
# para arredondar para cima math.floor(raiz)
# para aparecer 'x' casas decimais print('A raiz de {} é igual é {:.2f}'.format(num, raiz))


#Importação de partes de uma biblioteca

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual é {}'.format(num, (raiz)))


#Utilização de emoji

import emoji
print(emoji.emojize("Olá, Mundo :earth_anericas:", use_aliases=True))

# use_aliases=True permite uso de emojis fora do pac oficial