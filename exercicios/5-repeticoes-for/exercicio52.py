#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end = ' ')
        total += 1
    else:
        print('\033[31m', end = ' ')
    print('{} '.format(c), end = ' ')
print('\n\033[mExistem {} números divisíveis por {}.'.format(total, num))
if total == 2:
    print('O número {} é um número primo!'.format(num))
else:
    print('O número {} não é um número primo!'.format(num))