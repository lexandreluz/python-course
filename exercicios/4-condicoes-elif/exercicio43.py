#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 
# - Abaixo de 18.5: Abaixo do Peso 
# - Entre 18.5 e 25: Peso Ideal 
# - 25 até 30: Sobrepeso 
# - 30 até 40: Obesidade 
# - Acima de 40: Obesidade mórbida
print('='*39)
print('CALCULANDO SEU ÍNDICE DE MASSA CORPORAL')
print('='*39)
nome = str(input('Qual o seu nome? ')).title()
print('\nOlá {}, insira as informações a seguir para'.format(nome))
print('ver se o seu peso está ideal segundo a OMS')
print('Em metros, digite a sua altura.')
altura = float(input('(Ex: 1.70):  '))
print('Em quilograma, digite seu peso.')
peso = float(input('(Ex: 60.6):  '))
#calculando o IMC
imc = peso / (altura * altura)
#consições
print('{} seu IMC é {:.2f}'.format(nome, imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está acima do peso!')
elif imc >= 30 and imc < 40:
    print('Você está obeso!')
else:
    print('Você está com obesidade mórbida!')