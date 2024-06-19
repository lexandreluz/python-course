#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
print('=========== OPERAÇÕES ============')
number = int(input('Digite qualquer valor: '))

double = number * 2 
triple = number * 3
square = number ** 0.5 #pow(number,0.5)

print('O dobro desse número é {},'.format(double), end = ' ')
print('o triplo dele é {} e sua raiz quadrada é {:.0f}'.format(triple, square))