# Desenvolva um programa que leia o comprimento de três retas e digam ao usuário se elas podem ou não formar um Δ.

reta1 = float(input('Digite o valor da reta 1: '))
reta2 = float(input('Digite o valor da reta 2: '))
reta3 = float(input('Digite o valor da reta 3: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Pode formar um triângulo!')
else:
    print('Não pode formar um triângulo!')


# Reslução da aula
# print('-=-'*20)
# print('Analisador de Triângulos')
# print('-=-'*20)
# r1 = float(input('Primeiro segmento: '))
# r2 = float(input('Segundo segmento: '))
# r3 = float(input('Terceiro segmento: '))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print('Os segmentos PODEM FORMAR triângulo!')
# else:
#    print('Os segmentos NÃO PODEM FORMAR triângulo!')
