class Alumno: #creamos una clase 
    def __init__(self, nombre, promedio): #definimos el constructor de la clase y sus datos
        self.nombre = nombre
        self.promedio = promedio

    def saludar(self): #creamos funciones
        print("Hola soy", self.nombre, "y mi promedio es", self.promedio)

# Definimos objetos
a1 = Alumno("Fernando", 9.2)
a2 = Alumno("Maria", 8.5)

# Llamamos a las funciones de los objetos
a1.saludar()
a2.saludar()
