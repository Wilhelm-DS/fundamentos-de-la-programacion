'''
Programa para estudiar los elementos del lenguahje Python
Mi nombre es Guillermo Durán Sevilla
'''

nombre = "Juan"             #Variable tipo String
edad = 18                   #Vaiable tipo Integer
estatura = 1.67             #Variable tipo Float
es_estudiante = True        #Variable tipo Boolean

#Imprimimos la variable y su tipo
print("Nombre:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)
print("Es estudiante:", es_estudiante)

#Declaro una constante
PROMEDIO_MINIMO = 6.0       #Constante

#Introducimos datos y los guardamos en las variables materia y calificacion
materia = input("Ingrese el nombre de la materia: ")
nota = float(input("Ingrese la nota obtenida en " + materia + ": "))

#Hacemos operaciones matemáticas y lógicas
suma = 8 + 2
resto = 10 % 3
potencia = 2 ** 3

# Estamos declarando dos variables booleanas
mayor_de_edad = edad >= 18
aprobado = nota >= PROMEDIO_MINIMO and es_estudiante


# Imprimimos el resultado
print("Suma:", suma, "| Resto:", resto, "| Potencia:", potencia)
print("Mayor de edad:", mayor_de_edad)