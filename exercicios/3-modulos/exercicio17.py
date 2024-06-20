#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

print('====== ÁREA DO TRIÂNGULO =====')
op = float(input('Insira o comprimento do cateto oposto: '))
ad = float(input('Agora o comprimento do cateto adjacente: '))

#hip = math.sqrt(math.pow(op, 2) + math.pow(ad, 2))
hip = math.hypot(op,ad) #"math.hypot" função que calcula a hipotenusa

print('A comprimento da hipotenusa é {:.2f}.'.format(hip))