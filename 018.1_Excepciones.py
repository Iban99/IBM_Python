def indice(objeto, indice):
    print (objeto[indice])

try:
    print(indice('Python', 1))
except IndexError: 
    print('Has puesto un índice muy grande.')
print('Hemos salido del try-catch')




