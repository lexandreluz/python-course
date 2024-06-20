#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date # importar data

print('========= ANO BISSEXTO =========')

print('Quer saber se o ano é bissexto?')
ano = int(input('Digite o ano: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))
    
print('\nDica: Para saber se o ano é bissexto, basta verificar se \no resto da divisão por 4 é zero')