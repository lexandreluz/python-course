#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
print('=========== CVC - Sempre com você =========')
print('VEJA QUANTO SERÁ A SUA PASSAGEM')
distancia = float(input('Qual a distância do seu destino? '))

if distancia <= 200:
    p = distancia * 0.5
    print('O valor para sua viagem é R$ {:.2f}'.format(p))
else:
    p = distancia * 0.45
    print('O valor para a sua viagem R$ {:.2f}'.format(p))