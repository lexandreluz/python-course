#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

print(' ====== ÂNGULOS TRIGONOMÉTRICOS ======')
angle = float(input('Insira o valor do ângulo: '))
sin = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tag = math.tan(math.radians(angle))

#"math.sin,cos,tan" calcula o seno, o cosseno e a tangente respectivamente
#"math.radians" calcula o angulo em radiano

print('O valor do Cosseno é {:.2f}.'.format(cos))
print('O valor do Seno é {:.2f}.'.format(sin))
print('O valor da Tangente é {:.2f}.'.format(tag))