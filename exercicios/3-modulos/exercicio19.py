#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

print('===== ALUNO SORTUDO ======')
a1 = str(input('Primeiro aluno(a): '))
a2 = str(input('Segundo aluno(a): '))
a3 = str(input('Terceiro aluno(a): '))
a4 = str(input('Quarto aluno(a): '))

lista = [a1, a2, a3, a4]

lucky = random.choice(lista) # randomiza, escolhe alguma variavel especificada na lista

print('O aluno(a) sorteado é o(a) {}'.format(lucky))