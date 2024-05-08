# # Módulo math 
# import math
# math.sqrt(55)
# math.modf(222)

# # Módulo random
# import random
# random.random()
# lista = [1,5,8,9]
# random.choice(lista)
# random.shuffle(lista)
# lista

 
d={"50862634":37 , "43394932":32} 
texto = input("Introduce un documento de indentidad ")

if texto in d: 
    print("La edad de " + texto + " es " + str(d[texto]))
else:
    edad = input("Documento no existente. Introduce edad: ")
    if edad.isnumeric():
        num = int(edad)
        d[texto] = num
        print("Añadido al diccionario")

print(d)  

d["50862634"]