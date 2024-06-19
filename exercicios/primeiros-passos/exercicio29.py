#Escreva um programa que leia a velocidade de um carro.  Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.  A multa vai custar R$7,00 por cada Km acima do limite.
print('-*-' * 8)
print('VELOCIDADE DO CARRO')
print('-*-' * 8)

speed = float(input('Insira a velocidade do carro:'))

if speed > 80:
    print('Você ultrapassou o limite de velocidade!')
    multa = (speed - 80) * 7
    print('O valor de sua multa é R$ {:.2f}'.format(multa))
else: 
    print('Você está respeitando o limite de velocidade!')
    print('Tenha um bom dia! Dirija com segurança!')