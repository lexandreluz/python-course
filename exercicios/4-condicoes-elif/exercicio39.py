#Faça um programa que leia o ano de um jovem e informe, de acordo com sua idade: 
#- Se ele vai se alistar ao serviço militar 
#- Se é hora de se alistar 
#- Se já passou do tempo de alistamento. 
#- Seu programa também deverá mostrar o tempo que falta ou o prazo que faltou.

from datetime import date

print('============ YOU CAN DO IT ============')
print('Bem-vindo!\nVeja como está a sua condição no serviço militar.')
nome = str(input('Qual o seu nome? ')).title() # capitalização do nome inserido 
ano = int(input('Qual ano que você nasceu? '))

idade = date.today().year - ano # calcula a idade

print('\nOlá {}! Nesse ano você fará {} anos.'.format(nome, idade))

if idade < 18:
    print('Você só pode se alistar com 18 anos!')
    print('Ainda falta {} anos para você se alistar!'.format(18 - idade))
    print('Você só poderá se alistar em {}!'.format(date.today().year + (18 - idade)))
elif idade == 18:
    print('Prepare os seus documentos {}. Você se alista nesse ano!')
    print('Compareça a Junta de Serviço Militar mais próxima!')
else:
    print('Você já passou do ano ideal para alistamento!!!')
    print('Você deveria ter se alistado em {}'.format(date.today().year - (idade - 18)))
    print('Procure o quanto antes uma Junta de Serviço Militar para se regularizar')