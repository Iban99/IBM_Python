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

 
# d={"50862634":37 , "43394932":32} 
# texto = input("Introduce un documento de indentidad ")

# if texto in d: 
#     print("La edad de " + texto + " es " + str(d[texto]))
# else:
#     edad = input("Documento no existente. Introduce edad: ")
#     if edad.isnumeric():
#         num = int(edad)
#         d[texto] = num
#         print("Añadido al diccionario")

# print(d)  

# d["50862634"]

# for i in range(5):
#     print(i)

# tumail= input("Introduce tu mail: ")
# email=False
# for i in tumail:
#     if i == "@":
#         email=True

# for i in range(4):
#     print(f"Valor de la variable {i}")

# List = list()
# Set = set()
# l = int(input("Introduzca el tamaño de la 
# lista: "))
# s = int(input("Introduzca el tamaño del 
# Set: "))
# print("Introduzca los elementos de la 
# lista:")
# for i in range(0, 1):
#     list.append(int(input()))
# print("Introduzca los elementos del Set: 
# ")
# for i in range(0, 5):
#     Set.add(int(input()))
# print(list)
# print(set)

# test_tup=(7,8,9,1,10,7)
# print("The original tuple : " + str(test_tup))

# res = sum(list(test_tup))
# print (res)

class Persona:
    pass

#Declarar atributos fuera de la clase que pertenecen a ella
Persona.nombre = 'Ana'
Persona.edad = 30

persona = Persona()
persona.nombre

#Declarar métodos de la clase que pertenecen a ella
def presentarse(self):
    return f'Hola'

Persona.presentarse = presentarse