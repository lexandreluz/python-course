#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 a 500
cont = 0 
soma = 0
print('Insira os intervalos para saber a soma dos números divisiveis por 3')
i = int(input('Início: '))
f = int(input('Fim: '))
print('Os números divisiveis por 3 são: ')
print('*' * 5, end = ' ')
for contador in range(i, f + 1):
    if contador % 3 == 0 and contador % 2 == 1:
        cont = cont + 1  # contador que verifica a quantidade de numeros divisiveis por 3 e impares
        soma += contador   # soma todos os numeros divisiveis por 3 e impares
        print(contador, end = ' ')
print('*' * 5)
print('\nA soma de todos os {} números divisiveis por 3 de {} a {} é: {}'.format(cont, i, f, soma))