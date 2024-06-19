#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a sua idade: 
#- Até 9 anos: MIRIM 
#- Até 14 anos: INFANTIL 
#- Até 19 anos: JUNIOR 
#- Até 20 anos: SÊNIOR 
#- Acima: MASTER
from datetime import date

print('Bem vindo a competição anual de natação.')
nome = str(input('Qual o seu nome? ')).title()
print('\nOlá {}'.format(nome))
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
print('{} você tem {} anos! Certo?'.format(nome, idade))
if idade <= 9:
    print('Você faz parte da categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Você faz parte da categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Você faz parte da categoria JUNIOR')
elif idade > 19 and idade <= 20:
    print('Você faz parte da categoria SÊNIOR')
else:
    print('Você faz parte da categoria MASTER')