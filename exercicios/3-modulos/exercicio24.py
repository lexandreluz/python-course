#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
city = input('Em que cidade você nasceu? ').strip() #já verifica de tem espaços excedentes

city = city.title() #capitaliza todas as strings
print('Sua cidade: {}'.format(city))

#print(city[:5].upper() == 'SANTO')

city = city.upper().split() #Coloca tudo em maiusculo e divide a cadeia em uma lista para 
                            #analisar se tem SANTO no indice 0

if 'SANTO' in city[0]: # Verifica se tem SANTO no indice zero
    print('O nome da sua cidade começa com SANTO')
else:
    print('ERRORR')