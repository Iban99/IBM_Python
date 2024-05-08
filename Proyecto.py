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
lista_tareas = []
tarea = input("Introduce una nueva tarea: ")
if tarea not in lista_tareas:
    lista_tareas.append(tarea)
    print ("Tarea", tarea, "introducida a la lista")
    print (lista_tareas)
else:
    print ("La tarea ya está introducida")

lista_tareas[0]
lista_tareas_pendientes= {
    "1.Realizar módulo 'Fundamentos en Internet'":"Completada",
    "2.Realizar módulo 'Fundamentos en Programación'":"",
    "3.Realizar módulo 'Fundamentos en Desarrollo Web'":"",
    "4.Realizar módulo 'Fundamentos en GIT y GITHUB'":"",

    }

tarea_nueva = input('Introduce una nueva tarea: ')



