                             # CASO PRÁCTICO PYTHON FULL STACK #
'''
Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione 
una lista de tareas pendientes. El programa deberá permitir al usuario realizar las siguientes
operaciones:
    • Agregar una nueva tarea: El programa deberá permitir al usuario agregar una nueva tarea a
    la lista de tareas pendientes.
    • Marcar una tarea como completada: El programa deberá permitir al usuario marcar una
    tarea como completada, dada su posición en la lista.
    • Mostrar todas las tareas: El programa deberá imprimir en pantalla todas las tareas
    pendientes, numeradas y mostrando su estado (completada o pendiente).
    • Eliminar una tarea: El programa deberá permitir al usuario eliminar una tarea de la lista,
    dada su posición.

El programa deberá incluir las siguientes características:
• Manejo de excepciones: El programa deberá manejar excepciones en caso de que el
usuario ingrese una opción no válida o una posición que no exista en la lista.
• Comentarios explicativos: El código deberá estar comentado para explicar su
funcionamiento en cada parte relevante.
'''
#Creamos dos listas para que se diferencie bien entre tareas pendientes y completadas
lista_tareas_pendientes = list()
lista_tareas_completadas = list()

#Creamos dos variables de input, una la propia tarea, y la otra el estado
tarea = input("Introduce una nueva tarea: ")

#Se verifica que el estado sea válido
while True:
    estado = input("Introduce su estado (pendiente/completada): ")
    if estado in ["pendiente", "completada"]:
        break  # Salimos del bucle si el estado es válido
    else:
        print("El estado sólo puede ser 'pendiente' o 'completada'. Inténtalo de nuevo.")

#Bucle if en el que se comprueba si la tarea introducida está en alguna de las dos listas
#y a partir de aquí, agrega la tarea a la lista correspondiente según el estado
if tarea not in lista_tareas_completadas and tarea not in lista_tareas_pendientes:
    if estado == "pendiente":
        lista_tareas_pendientes.append(tarea)
        print(f'La tarea se añadió a la lista_tareas_pendientes')
    elif estado == "completada":
        lista_tareas_completadas.append(tarea)
        print(f'La tarea se añadió a la lista_tareas_completadas')
    print (f'Pendientes: {lista_tareas_pendientes}')
    print (f'Completadas: {lista_tareas_completadas}')
#Si la tarea ya existe en alguna de las listas, nos salta el print del else.
else:
    print ("La tarea ya está introducida")


