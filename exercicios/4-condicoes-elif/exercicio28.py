#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint # biblioteca que escolhe aleatoriamente um intervalo de strings especificados
from time import sleep # biblioteca que especifica um periodo de tempo
print('=' * 20)
print('JOGO DA ADIVINHAÇÃO')
print('=' * 20)
print('Vou pensar em um número de 1 a 5. Tente adivinhar...')

n = randint(1, 5) # o computador escolhe em um numero de 1 a 5
palpite = int(input('\nEm que número pensei? '))
if palpite > 5:
    print('\nVocê tem que digitar um número entre 1 e 5!')
if palpite >= 1 and palpite <= 5:
    print('PROCESSANDO... ')
    sleep(2) # espera 2 segundos
    print('O número que pensei foi o {} e você chutou no {}'.format(n, palpite))
    if palpite == n:
        print('\nPARABÉNS, você acertou!')
    else:
        print('\nGANHEI, você errou. Try again!')