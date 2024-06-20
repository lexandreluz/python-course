#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: 
#- O primeiro valor é maior 
#- O segundo valor é maior 
#- Não existe valor maior, os dois são iguais
print('======= MAIOR NÚMERO ========')
print('Insira os números que você quer comparar.')
numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))

if numero1 > numero2:
    print('O número {} é maior que o número {}'.format(numero1, numero2))
elif numero2 > numero1:
    print('O número {} é maior que o número {}'.format(numero2, numero1))
else:
    print('Os dois números digitados é o {}. Eles são iguais.'.format(numero1))