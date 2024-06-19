#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Insira o texto: ').strip().upper() # coloca a frase em maiusculo e exclui os
                                                  # espaços excedentes

print('Tem {} letras A nessa frase'.format(frase.count('A'))) #confere quantas letras A tem na frase
print('A primeira posição do A é: {}'.format(frase.find('A') + 1)) #encontra a primeira ocorrencia do A
print('A última posição do A é: {}'.format(frase.rfind('A') + 1)) #encontra a primeira ocorrencia do 
                                                                    # A da direita para a esquerda