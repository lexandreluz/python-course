# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher
print('=============== TABUADA ================')
number = int(input('Olá! Qual tabuada você quer saber? '))
print('\n=Tabuada de {} ='.format(number))

for i in range (1, 11):
    tab = number * i
    print('{} * {} = {}'.format(i, number, tab))
print('---------------------')
print('Aí está a tabuada de {}'.format(number))