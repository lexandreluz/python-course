#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
valor = float(input('Insira um comprimento em metros: '))

cm = valor / 100
mm = valor / 1000

print('O valor em centímetros é {} e em milímetros é {}'.format(cm, mm))