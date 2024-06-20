#Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2para octal e 3 para hexadecimal
print('=========== CONVERSÃO ============')
print('Escolha o tipo de Conversão:')
print('[ 1 ] Binário \n[ 2 ] Octal \n[ 3 ] Hexadecimal')
option = int(input('Qual sua escolha? '))
number = int(input('Qual o número para a conversão? '))

if option == 1:
    print('O número {} em binário é {}'.format(number, bin(number)))
elif option == 2:
    print('O número {} em octal é {}'.format(number, oct(number)))
elif option == 3:
    print('O número {} em hexadecimal é {}'.format(number, hex(number).title()))
else:
    print('Opção não existente! Tente as opções sugeridas.')