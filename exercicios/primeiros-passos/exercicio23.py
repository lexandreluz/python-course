#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
number = int(input('Digite um número: '))
u = number // 1 % 10 
d = number // 10 % 10 
c = number // 100 % 10 
m = number // 1000 % 10 

if number <= 9999:
    print('''
    Unidade: {}
    Dezena: {}
    Centana: {}
    Milhar: {}'''.format(u, d, c, m))
    
else:
        print('Digite apenas números abaixo de 10000')