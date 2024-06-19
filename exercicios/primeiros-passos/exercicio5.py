# Crie um programa que leia dois números e mostre a soma entre eles. Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
print('========= ANTECESSOR E SUCESSOR =========')
number = int(input('Digite qualquer número: '))

ant = number - 1
post = number + 1

print('O antercessor é {} e o sucessor é {}'.format(ant, post))

#print('O antercessor é {} e o sucessor é {}'.format((n - 1) + (n + 1))