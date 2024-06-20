#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
import math

print('======== ARREDONDAMENTO ========')
number = float(input('Digite um número: '))

print('\nA parte inteira de {} é {}'.format(number , math.trunc(number)))
#"math.trunc" elimina todos os valores depois da virgula

#print('\nA parte inteira de {} é {}'.format(number , math.floor(number)))
#"math.floor" arredonda o numero para baixo