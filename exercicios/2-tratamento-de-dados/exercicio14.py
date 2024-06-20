#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
print('==== CONVERSOR DE TEMPERATURA ====')
temp = float(input('Insira o temperatura em Celsius: '))

kel = temp + 273.15
fah = 1.8 * temp + 32

print('A temperatura em Kelvin é de {}° e em Fahrenheit é {}°'.format(kel, fah))