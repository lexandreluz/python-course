#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária pata pintá-la, sabendo que cada litro  de tinta pinta uma área de 2 metros quadrados.
print('========== QUANTIDADE DE TINTA ===========')
lar = float(input('Digite a largura da parede: '))
alt = float(input('Agora digite a altura da parede: '))

area = lar * alt
tinta = area / 2

print('A área da parede é de {} m² e você vai precisar de {} litros de tinta para pintá-la'.format(area, tinta))