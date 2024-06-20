#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
print('============ EMPRÉSTIMO ===========')
nome = str(input('Qual o seu nome?' )).title()
print('\nOlá {}, agora insira os dados a seguir...'.format(nome))
valor = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você pretende pagar? '))
print('\nObrigado pelas informações {}'.format(nome))

valorParcela = valor / (anos * 12)
percentualSalario = salario * 0.3
print('\n{} sua parcela é de R$ {:.2f}'.format(nome, valorParcela))

if valorParcela <= percentualSalario:
    print('Seu empréstimo foi CONCEDIDO! Parabéns!')
else:
    print('Seu empréstimo foi NEGADO!')
    print('Tente ver as possibilidades de parcelamento ou uma casa mais em conta ;)')