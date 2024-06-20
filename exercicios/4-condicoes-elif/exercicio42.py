#Refaça o desafio 035 dos triâgulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
# - Equilátero: todos os lados iguais 
# - Isósceles: dois lados iguais 
# - Escaleno: todos os lados diferentes
'''Para construir um triângulo é necessário que a medida de qualquer um dos lados seja 
menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença
 entre essas medidas.'''

print('======== ANALISANDO O TRIÂNGULO =========')

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('Os segmentos podem formar um triânulo!!!!')
    if a == b and b == c:
        print('Analisando o triângulo pode-se dizer que ele é EQUILÁTERO')
    elif a == b and b != c or b == c and c != a or c == a and a != b:
        print('Analisando o triângulo pode-se dizer que ele é ISÓSCELES')
    else:
        print('Analizando o triângulo pode-se dizer que ele é ESCALENO')
else:
    print('ERROR')