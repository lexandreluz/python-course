#Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagemno final, de acordo com a média atingida: 
#- Média abaixo de 5.0: REPROVADO 
#- Média entre 5.0 e 6.9: RECUPERAÇÃO  
#- Média 7.0 ou superior: APROVADO

print('='*10,' BOLETIM ESCOLAR ','='*10)
nota1 = float(input('Qual foi a sua primeira nota? '))
nota2 = float(input('Qual foi a sua segunda nota? '))

media = (nota1 + nota2) / 2

if media < 5:
    print('\nQue pena, sua nota não foi boa!')
    print('Você está REPROVADO, sua média é {}'.format(media))
    print('Se esforce mais no próximo ano ;)')
elif media >= 5 and media < 7:
    print('\nHmmmm... Sua nota não foi muito boa!')
    print('Sua média é {}'.format(media))
    print('Você está de RECUPERAÇÃO!')
else:
    print('\nMuito bem! Sua média é {}'.format(media))
    print('Você está APROVADO!')