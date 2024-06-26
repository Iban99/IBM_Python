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
    #Inicialización de los atributos de la clase. Constructor.
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
                color = "\033[92m" if tareas["completada"] else "\033[91m"  
                reset = "\033[0m"
                print(f"{i + 1}. {color}{tareas['descripcion']} - {estado}{reset}")
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
    nombre= input("¡Bienvenid@! Indícame por favor, ¿Cuál es tu nombre? ")

    #Creamos un bucle infinito para poder mostrar las opciones del programa
    while True:
        print('\033[1m' + 'Bienvenid@ al Gestor de Tareas'+ '\033[0m')
        print(" ")
        print('1. Agregar una nueva tarea a la lista')
        print('2. Marcar una tarea como completada')
        print('3. Visualizar toda la lista de tareas')
        print('4. Eliminar una tarea existente')
        print('5. Salir del programa')
        print(" ")
        
        #Manejo de excepciones, con try y except
        try:
            #Le pedimos al usuario que introduzca la opcion de la lista que desea realizar
            opcion = int(input("Selecciona una opción según su número: "))
            
            #Bucle if, con todas las opciones disponibles en la lista
            if opcion == 1:
                #Esta opcion va a permitir introducir una nueva tarea a la lista llamando al método 
                #agg_tarea de la clase GestorTareas. 
                while True:
                    #El bucle para introducir de 1 vez tantas como se quiera.
                        print(" ")
                        descr_tarea = input(f'Perfecto {nombre}, ya puede introducir la nueva tarea a la lista: ')
                        gestor.agg_tarea(descr_tarea) 
                        print(" ")
                        gestor.ver_tareas()
                        print(" ")
                        #Condicional para poder volver a introducir otra tarea
                        agregar_otra = input('¿Quieres agregar otra tarea (si/no): ').strip().lower()
                        if agregar_otra == 'si':
                            continue
                        elif agregar_otra != 'si':
                            break
                                       
            elif opcion == 2:
                #Esta opción nos va a permitir marcar una tarea completada llamando al método
                #tarea_completada
                print(" ")
                gestor.ver_tareas()
                indice = int(input(f"¨{nombre}, selecciona el número de la tarea que quiere marcar como completada: "))
                #Esta variable es necesaria, ya que sino al introducir el índice, como el diccionario inicializa en 0, nos
                #marcaría un error.
                indice_interno = indice - 1
                gestor.tarea_completada(indice_interno)
                
            elif opcion == 3:
                #Esta opción nos va a permitir ver toda la lista de las tareas y su estado llamando al
                #método ver_tareas
                print(" ")
                gestor.ver_tareas()
            
            elif opcion == 4:
                #Esta opción nos va a permitir eliminar una tarea de la lista llamando al método
                #eliminar_tarea
                print(" ")
                gestor.ver_tareas()
                tarea_a_eliminar = int(input(f"{nombre}, selecciona el número de la tarea que quiere eliminar: "))
                numero_interno= tarea_a_eliminar - 1
                gestor.eliminar_tarea(numero_interno)
            
            elif opcion == 5:
                #Esta opción nos va a permitir salir del bucle WHILE
                print(" ")
                print(f'{nombre}, muchas gracias por usar este programa, nos vemos pronto.')
                print('¡Hasta pronto!')
                break
            
            else:
                #En el caso de que el número introducido no esté en la lista
                print(" ")
                print("La opción seleccionada no es válida. Por favor, vuelva a probar.")
        
        except ValueError:
            #En el caso de que el dato que introduzca el usuario no sea un número
            print(" ")
            print('\033[1;31m' + 'Error: El caracter introducido no es válido. Introduce un número.' + '\033[0m')

main()
    



        
        
        

    