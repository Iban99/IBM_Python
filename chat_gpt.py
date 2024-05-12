class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        self.tasks.append({"description": task_description, "completed": False})

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
        else:
            print("Error: Índice de tarea inválido.")

    def show_tasks(self):
        if self.tasks:
            print("Tareas pendientes:")
            for i, task in enumerate(self.tasks):
                status = "Completada" if task["completed"] else "Pendiente"
                print(f"{i + 1}. {task['description']} - {status}")
        else:
            print("No hay tareas pendientes.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Error: Índice de tarea inválido.")


# Función principal del programa
def main():
    manager = TaskManager()

    while True:
        print("\n=== Gestor de Tareas ===")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")

        try:
            option = int(input("Seleccione una opción: "))

            if option == 1:
                task_description = input("Ingrese la descripción de la nueva tarea: ")
                manager.add_task(task_description)
            elif option == 2:
                manager.show_tasks()
                task_index = int(input("Ingrese el número de la tarea completada: ")) - 1
                manager.complete_task(task_index)
            elif option == 3:
                manager.show_tasks()
            elif option == 4:
                manager.show_tasks()
                task_index = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
                manager.delete_task(task_index)
            elif option == 5:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()

#----------------------------------------------------------------------------------------------------#
# class ListaTareas:
#     def __init__(self):
#         self.tareas = []

#     def agregar_tarea(self, nueva_tarea):
#         self.tareas.append({"nombre": nueva_tarea, "completada": False})

#     def marcar_completada(self, indice):
#         try:
#             self.tareas[indice]["completada"] = True
#         except IndexError:
#             print("¡El índice está fuera de rango!")

#     def marcar_pendiente(self, indice):
#         try:
#             self.tareas[indice]["completada"] = False
#         except IndexError:
#             print("¡El índice está fuera de rango!")

#     def mostrar_tareas(self):
#         if not self.tareas:
#             print("No hay tareas en la lista.")
#         else:
#             for i, tarea in enumerate(self.tareas):
#                 estado = "Completada" if tarea["completada"] else "Pendiente"
#                 print(f"{i + 1}. {tarea['nombre']} - {estado}")

# # Ejemplo de uso
# lista_tareas = ListaTareas()

# while True:
#     print("\n1. Agregar tarea")
#     print("2. Marcar tarea como completada")
#     print("3. Marcar tarea como pendiente")
#     print("4. Mostrar todas las tareas")
#     print("5. Salir")

#     opcion = input("\nSeleccione una opción: ")

#     if opcion == "1":
#         nueva_tarea = input("Ingrese la nueva tarea: ")
#         lista_tareas.agregar_tarea(nueva_tarea)
#     elif opcion == "2":
#         indice = int(input("Ingrese el índice de la tarea a marcar como completada: ")) - 1
#         lista_tareas.marcar_completada(indice)
#     elif opcion == "3":
#         indice = int(input("Ingrese el índice de la tarea a marcar como pendiente: ")) - 1
#         lista_tareas.marcar_pendiente(indice)
#     elif opcion == "4":
#         lista_tareas.mostrar_tareas()
#     elif opcion == "5":
#         print("Saliendo...")
#         break
#     else:
#         print("Opción inválida. Por favor, seleccione una opción válida.")


class GestorTareas:
    def __init__(self):
        self.lista_tareas_pendientes = []
        self.lista_tareas_completadas = []

    def agregar_tarea(self, tarea, estado):
        while True:
            if estado in ["pendiente", "completada"]:
                break
            else:
                print("El estado solo puede ser 'pendiente' o 'completada'. Inténtalo de nuevo.")
                estado = input("Introduce su estado (pendiente/completada): ")

        if tarea not in self.lista_tareas_completadas and tarea not in self.lista_tareas_pendientes:
            if estado == "pendiente":
                self.lista_tareas_pendientes.append(tarea)
                print('La tarea se añadió a la lista de tareas pendientes')
            elif estado == "completada":
                self.lista_tareas_completadas.append(tarea)
                print('La tarea se añadió a la lista de tareas completadas')
            self.mostrar_tareas()
        else:
            print("La tarea ya está introducida")

    def mostrar_tareas(self):
        print('Pendientes:', self.lista_tareas_pendientes)
        print('Completadas:', self.lista_tareas_completadas)
    
    def mostrar_tareas(self):
        print('Tareas Pendientes:')
        for i, tarea in enumerate(self.lista_tareas_pendientes, 1):
            print(f'{i}. {tarea}')
        print('Tareas Completadas:')
        for i, tarea in enumerate(self.lista_tareas_completadas, 1):
            print(f'{i}. {tarea}')



# Ejemplo de uso
gestor = GestorTareas()
tarea = input("Introduce una nueva tarea: ")
estado = input("Introduce su estado (pendiente/completada): ")
gestor.agregar_tarea(tarea, estado)
