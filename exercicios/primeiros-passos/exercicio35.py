#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''Para construir um triângulo é necessário que a medida de qualquer um dos lados seja 
menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença
 entre essas medidas.'''

print('======== ANALISANDO O TRIÂNGULO =========')

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('Os segmentos podem formar um triânulo!!!!')
else:
    print('ERROR')