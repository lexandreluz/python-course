#Desenvolva um programa que leia seis números inteiros e mostre a soma daqueles que forem pares. Se o valor digitado for impar, desconsidere-o
cont = 0
soma = 0
for contador in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        cont = cont + 1
        soma += n
print('\nDos seis números que você digitou apenas {} são pares.'.format(cont))
print('E a soma dos seis números é: {}'.format(soma))