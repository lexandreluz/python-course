#Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 a 50
print('DESCUBRA OS NÚMEROS PARES OU ÍMPARES DE UM INTERVALO DE NÚMEROS')
i = int(input('Início: '))
f = int(input('Fim: '))

print('\n[ 1 ] - ÍMPAR')
print('[ 2 ] - PAR')
option = int(input('Escolha uma opção: '))

if option == 1:
    for c in range (i, f+1):         # o contador confere do inicio ao fim 
        impar = c % 2                # verfifica o resto da divisão
        if impar == 1:               # verifica de o resto da divisão é 1
            print(c, end = ' - ')

    print('\nAí está os números ímpares de {} a {}'.format(i, f))
elif option == 2:
    for c in range (i, f+1):          # o contador confere do inicio ao fim
        par = c % 2                   # verfifica o resto da divisão
        if par == 0:                  # verifica de o resto da divisão é 1
            print(c, end=' - ')

    print('\n Aí está os números pares de {} a {}'.format(i, f))
else:
    print('Digite 1 ou 2')