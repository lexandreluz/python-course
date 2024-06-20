# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Agora a segunda: '))

media = (nota1 + nota2) / 2

print('Sua média é {}'.format(media))

if media < 5: 
    print('Que pena! Se esforce da próxima vez!')
    
else: 
    print('Parabéns!!!!')