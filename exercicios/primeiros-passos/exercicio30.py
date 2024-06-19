#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('='*15)
print('É PAR OU ÍMPAR?')
print('='*15)

print('Quer saber se o número é par ou impar?')
n = int(input('Digite um número: '))

if n%2 == 1:
    print('O número {} é ÍMPAR'.format(n))
else:
    print('O número {} é PAR'.format(n))