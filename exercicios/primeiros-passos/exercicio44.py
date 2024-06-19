#Elabore um programa que calcule o valor a se pago por um produto, considerando o seu preço normal e condição de pagamento: 
# - à vista no cartão: 5% de desconto 
# - em até 2x no cartão: preço normal 
# - 3X ou mais no cartão: 20% de juros

print('============= CAIXA 64 ============')
valor = float(input('Preço das compras: R$ '))
print('ESCOLHA A FORMA DE PAGAMENTO')
print('[ 1 ] - à vista dinheiro/cheque')
print('[ 2 ] - à vista cartão')
print('[ 3 ] - parcelado no cartão')
option = int(input('Qual a opção? '))

if option == 1:
    total = valor - (valor * 0.1)
    print('Suas compras são R${:.2f}'.format(valor))
    print('Sua compra vai custar R${:.2f}'.format(total))
elif option == 2:
    total = valor - (valor * 0.05)
    print('Suas compras são R${:.2f}'.format(valor))
    print('Sua compra vai custar R${:.2f}'.format(total))
elif option == 3:
    parcelas = int(input('Em quantas parcelas você deseja pagar? '))
    if parcelas < 2:
        print('Só parcelamos a partir de 2 parcelas!')
    elif parcelas == 2:
        print('Sua compra vai custar R${:.2f}'.format(valor))
    else:
        par = valor / parcelas
        juros = (par * 0.2) + par
        total = juros * parcelas  
        print('Sua compra parcelada em {:.0f}x será R$ {:.2f} com juros'.format(parcelas, juros))
        print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(valor, total))
else:
    print('Escolha uma opção de 1 a 3!')