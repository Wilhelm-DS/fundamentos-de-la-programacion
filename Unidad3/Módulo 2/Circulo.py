import math

radio = float(input("Radio del círculo: "))

area = math.pi * math.pow(radio, 2)
perimetro = 2 * math.pi * radio

print("Área", round(area, 2))
print("Perímetro", round(perimetro, 2))
print("Raíz cuadrada del área:", round(math.sqrt(area), 2))
print("Techo del área:", round(math.ceil(area), 2))

#---------------------------------------------------------------------------------------------------------------------------#

'''Explque cómo funciona la línea 1:'''

# La línea 1 del código, [import math], le pide a Python que importe el módulo de [math], que contiene funciones matemáticas.
    # Al ser una librería estándar, Python no necesita que se le defina el archivo del que viene, 
    # por ello solo se usa la función [import], saltándose la función [from].

#---------------------------------------------------------------------------------------------------------------------------#

'''Ejemplo de la función potencia:'''

x = float(input("Ingrese el valor de X: "))
y = float(input("Ingrese el valor de Y: "))

print("X elevado a Y:", math.pow(x, y))

#---------------------------------------------------------------------------------------------------------------------------#

'''Ejemplo de la función raíz cuadrada:'''

x = float(input("Ingrese el valor de X: "))
print("Raíz cuadrada de X:", math.sqrt(x))