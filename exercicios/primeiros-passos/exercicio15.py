#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('====== ALUGUEL DE CARROS ======')
km = float(input('Qual a distância para o seu destido? '))
temp = float(input('Por quantos dias você irá usar o veículo? '))

valor = (km * 0.15) + (temp * 60)

print('O valor do aluguel nessas condições é de R$ {:.2f}'.format(valor))
print('Agradecemos a preferência!')