


# POO

# CONSTRUCTORES CON PARÁMETROS

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Juan', 'Perez', 28)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
    
    def descricpion(self):
        return f"{self.titulo}por {self.autor}"
    
    def is_antiguo(self):
        return self.anio_publicacion < 1910

libro1 = Libro('1', 'Juan', 1967)
libro2 = Libro('2', 'Jose', 1605)

libro1.is_antiguo()
libro2.is_antiguo()