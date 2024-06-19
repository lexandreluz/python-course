#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
name = input("Digite seu nome completo: ").strip().title()

n = name.split() # divide as strings em listas

print("Olá {}".format(name))
print('Seu primeiro nome é {}'.format(n[0])) #mostra a primeira posição da lista
print('Seu último nome é {}'.format(n[len(n)-1])) #mostra a ultima posiçao da lista,