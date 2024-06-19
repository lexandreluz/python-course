#Crie um programa que faça o computador jogar Jokenpô com você - Pedra, Papel, Tesoura, Lagarto, Spock

import random # biblioteca que escolhe aleatoriamente um intervalo de strings especificados
from time import sleep # biblioteca que especifica um periodo de tempo

print('============ JOKENPÔ ===========')
print("Let's play?")
user = str(input('What do you choose? ')).lower()

paper = 'paper'
scissor = 'scissor'
rock = 'rock'
lizard  = 'lizard'
spock = 'spock'

jokenpo = [paper, scissor, rock, lizard, spock]
# choice escolhe uma variavel aleatoria de jokenpo
n = random.choice(jokenpo)

print('\nROCK')
sleep(0.5)
print('PAPER')
sleep(0.5)
print('SCISSOR')
sleep(0.5)
print('LIZARD')
sleep(0.5)
print('SPOCK')
sleep(0.5)

print('\nYou chose {}'.format(user))
print('And I chose {}'.format(n))

if 'paper' in user and 'rock' in n or 'paper' in user and 'spock' in n or 'scissor' in user and 'paper' in n or 'scissor' in user and 'lizard' in n or 'rock' in user and 'scissor' in n or 'rock' in user and 'lizard' in n or 'lizard' in user and 'spock' in n or 'lizard' in user and 'paper' in n or 'spoke' in user and ' scissor' in n or 'spoke' in user and 'rock' in n:
    print('\nCongrats! You win!!!')
elif 'paper' in user and 'paper' in n or 'scissor' in user and 'scissor' in n or 'rock' in user and 'rock' in n or 'lizard' in user and 'lizard' in n or 'spock' in user and 'spock' in n:
    print("\nDam it! Tied, let's go again")
else:
    print('\nHa ha!!! I won')