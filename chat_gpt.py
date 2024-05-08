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
