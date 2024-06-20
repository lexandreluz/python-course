#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
print('========== SALÁRIO ============')
earn = float(input('Insira seu Salário: '))
 
new = (earn * 0.15) + earn
 
print('Seu novo sálario é de R$ {:.2f}'.format(new))