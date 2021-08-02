frase = 'Curso em Vídeo Python'
print(frase[3])  # printa a quarta letra
print(frase[:13])  # fatiamento
print(frase.count('o'))  # conta quantas letras o número de letras o
print(frase.upper().count('O'))  # transforma em caixa alta e conta o números de letras O
print(len(frase))  # conta o tamanho da frase
print(frase.replace('Python', 'Android'))  # substitui a palavra Python por Android
print('Curso' in frase)  # verifica a existência da palavra Curso na frase
print(frase.find('Vídeo'))  # verifica a posição da palavra dentro da frase
print(frase.lower().find('vídeo'))  # transforma a string toda em letras minúsculas e verificia se há vídeo nela


frase = '  Curso em Vídeo Python  '
print(len(frase.strip()))  # conta o tamanho da frase sem os espaços


print('Oi')

print("""Mussum Ipsum, cacilds vidis litro abertis. 
Viva Forevis aptent taciti sociosqu ad litora torquent. 
Per aumento de cachacis, eu reclamis. Casamentiss faiz malandris se pirulitá. 
Quem manda na minha terra sou euzis!""")


frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido)
# print(dividido[0]) -> mostra o que está na divisão 0
print(dividido[2][3])  # mostra a letra 3 da parte 2 da divisão da string