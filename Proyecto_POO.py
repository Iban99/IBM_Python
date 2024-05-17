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
    #Inicialización de los atributos de la instancia. Constructor.
    def __init__ (self):
        self.tareas = []
    
    #Creamos el método para poder agregar una tarea a la lista
    def agg_tarea(self, descr_tarea):
        self.tareas.append({"descripcion": [descr_tarea], "completada": False})
    
    #Creamos el método para poder marcar una tarea como completada
    def tarea_completada(self, indice):
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
            print("De momento, no existe ninguna tarea en la lista.")
    
    #Creamos el método para eliminar la tarea deseada de la lista
    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
        else:
            print("Error: el índice indicado no existe.")
        

# Programa, función principal
def main():
    #Instancia de la Clase GestorTareas, creando el objeto gestor
    gestor = GestorTareas()
    #Le pido al usuario que introduzca el nombre para poder interactuar
    nombre= input("¡Bienvenid@!¿Indícame por favor, ¿Cuál es tu nombre? ")

    #Creamos un bucle infinito para poder mostrar las opciones del programa
    while True:
        print('\nBienvenido al Gestor de Tareas')
        print(" ")
        print('1. Agregar una nueva tarea a la lista')
        print('2. Marcar una tarea como completada')
        print('3. Visualizar toda la lista de tareas')
        print('4. Eliminar una tarea existente')
        print('5. Salir del programa')
        
        #Manejo de excepciones, con try y except
        try:
            #Le pedimos al usuario que introduzca la opcion de la lista que desea realizar
            opcion = int(input("Selecciona una opción según su número:"))
            
            #Bucle if, con todas las opciones disponibles en la lista
            if opcion == 1:
                #Esta opcion va a permitir introducir una nueva tarea a la lista llamando al método 
                #agg_tarea de la clase GestorTareas
                descr_tarea = input(f'Perfecto {nombre}, ya puede introducir la nueva tarea a la lista: ')
                gestor.agg_tarea(descr_tarea) 
                gestor.ver_tareas()
                
            elif opcion == 2:
                #Esta opción nos va a permitir marcar una tarea completada llamando al método
                #tarea_completada
                gestor.ver_tareas()
                indice = int(input(f"¨{nombre}, selecciona el número de la tarea que quiere marcar como completada: "))
                #Esta variable es necesaria, ya que sino al introducir el índice, como el diccionario inicializa en 0, nos
                #marcaría un error.
                indice_interno = indice - 1
                gestor.tarea_completada(indice_interno)
                
            elif opcion == 3:
                #Esta opción nos va a permitir ver toda la lista de las tareas y su estado llamando al
                #método ver_tareas
                print("\nLista de tareas:")
                gestor.ver_tareas()
            
            elif opcion == 4:
                #Esta opción nos va a permitir eliminar una tarea de la lista llamando al método
                #eliminar_tarea
                gestor.ver_tareas()
                tarea_a_eliminar = int(input(f"{nombre}, selecciona el número de la tarea que quiere eliminar: "))
            
            elif opcion == 5:
                #Esta opción nos va a permitir salir del bucle WHILE
                print(f'{nombre}, muchas gracias por usar este programa, nos vemos pronto')
                print('¡Hasta pronto!')
                break
            
            else:
                #En el caso de que el número introducido no esté en la lista
                print("La opción seleccionada no es válida. Por favor, vuelva a probar.")
        
        except ValueError:
            #En el caso de que el dato que introduzca el usuario no sea un número
            print("Error: El caracter introducido no es válido. Introduce un número")

main()
    



        
        
        
