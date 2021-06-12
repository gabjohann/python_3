# Escreva um programa que converta uma temperatura digitada em °C para graus Fahrenheit

celcius = float(input('Está quantos graus °C? '))
fahrenheit = ((9 * celcius) / 5) + 32
print('{}°C equivalem a {}°F'.format(celcius, fahrenheit))
