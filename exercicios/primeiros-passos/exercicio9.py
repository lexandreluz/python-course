#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
print('=============== TABUADA ================')
number = int(input('Olá! Qual tabuada você quer saber? '))
print('\n=Tabuada de {} ='.format(number))

for i in range (1, 11):
    tab = number * i
    print('{} * {} = {}'.format(i, number, tab))
print('---------------------')
print('Aí está a tabuada de {}'.format(number))