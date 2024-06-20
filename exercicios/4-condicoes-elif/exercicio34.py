#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print('============ BONIFICAÇÃO ===========')
print('Veja quanto será o seu salário com o aumento')
salario = float(input('Qual o valor so seu salário? R$ '))

if salario > 1250:
    novosalario = (salario * 0.10) + salario
    print('O seu aumento é de R$ {:.2f}'.format(salario * 0.1))
    print('O seu salário agora é R$ {:.2f}'.format(novosalario))
    
else:
    novosalario = (salario * 0.15) + salario
    print('O seu aumento é de R$ {:.2f}'.format(salario * 0.15))
    print('O seu salário agora é R$ {:.2f}'.format(novosalario))