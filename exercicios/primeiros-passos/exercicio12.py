#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
print('=============== DESCONTO ================')
prod = float(input('Insira o valor do produto: '))

val = (prod * 5)/100
des = prod - val

print('Seu desconto é de R$ {:.2f}'.format(val))
print('Agora você só vai pagar R$ {:.2f}'.format(des))