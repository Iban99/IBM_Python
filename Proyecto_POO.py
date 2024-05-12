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

class GestorTareas:
    def __init__ (self):
        self.tareas = []
    
    def agg_tarea(self, descr_tarea):
        self.tareas.append(f'descripcion: {descr_tarea}, completed: False')
        
    def completa_tarea(self, estado):
        if estado == 'completado':
            self.tareas[estado.lower]["completado"] = True
        else:
            print("Error: una tarea sólo puede estar pendiente o completada.")
            
    def ver_tareas(self):
        if self.tareas:
            print("Lista de tareas:")
            for i, tareas in enumerate(self.tasks):
                status = "Completada" if task["completed"] else "Pendiente"
                print(f"{i + 1}. {task['description']} - {status}")
        else:
            print("No hay tareas pendientes.")
    