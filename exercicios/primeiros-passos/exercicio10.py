#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
print('=============== CONVERSOR ================')
valor = float(input('Quanto você tem em R$? '))

dol = valor * 4.07
eur = valor * 4.53
lib = valor * 5.34

print('Você pode comprar $ {} em dólar, £ {} em libra e € {} em euros'.format(dol, lib, eur))