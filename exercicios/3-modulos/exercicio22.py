#Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas;

#– Quantas letras ao todo (sem considerar espaços);

#– Quantas letras tem o primeiro nome.

print('============================')
nome = input('Insira seu nome completo: ').strip() #exclui os espaços excedentes, antes e depois da cadeia

print(nome.title()) #escreve na tela o nome capitalizado
print('Seu nome em maiusculo fica ({})'.format(nome.upper())) #escreve o nome em maiusculo
print('Seu nome em minúsculo fica ({})'.format(nome.lower())) #escreve o nome em minusculo

print('O seu nome tem {} letras'.format(len(nome) - nome.count(' '))) #confere quantas strings
                                                                      #tem na cadeia sem considerar
                                                                      #os espaços

nome = nome.split() #divide a cadeia em listas
print('O seu primeiro nome tem {} letras'.format(len(nome[0]))) #confere quantas letras tem 
                                                                #o primeiro nome digitado