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
#Creamos la CLASE de GESTOR DE TAREAS 
class GestorTareas:
    #Inicialización de los atributos de la instancia
    def __init__ (self):
        self.tareas = []
    
    #Creamos el método para poder agregar una tarea a la lista
    def agg_tarea(self, descr_tarea):
        self.tareas.append({"Tarea: " [descr_tarea], "completada: " False})
    
    #Creamos el método para poder marcar una tarea como completada
    def marcar_tarea_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True
        else:
            print("Error: el índice indicado no existe.")
    
    #Creamos el método para poder ver todas las tareas de la lista
    def ver_tareas(self):
        if self.tareas:
            print("Lista de tareas:")
            for i, tareas in enumerate(self.tareas):
                estado = "completada" if tareas["completada"] else "Pendiente"
                print(f"{i + 1}. {tareas['descripcion']} - {estado}")
        else:
            print("No existe ninguna tarea en la lista.")
    
    #Creamos el método para eliminar la tarea deseada de la lista
    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
        else:
            print("Error: el índice indicado no existe.")
        

# Programa, función principal
def main():
    gestor = GestorTareas()
    nombre_usuario= input("\033[1;34mprint('¡Bienvenid@!¿Cuál es tu nombre?')\033[0m")

    while True:
        print("\033[1;34mprint('Bienvenido al Gestor de Tareas')\033[0m")
        print("\033[1mprint('1. Agregar una nueva tarea a la lista')\033[0m")
        print("\033[1mprint('2. Marcar una tarea como completada')\033[0m")
        print("\033[1mprint('3. Visualizar toda la lista de tareas')\033[0m")
        print("\033[1mprint('4. Eliminar una tarea existente')\033[0m")
        print("\033[1mprint('5. Salir del programa')\033[0m")
        
        try:
            opcion = int(input("Selecciona una opción según su número:"))
            
            if opcion == 1
            
            elif opcion == 2
            
            elif opcion == 3
            
            elif opcion == 4
            
            elif opcion == 5
        
        except