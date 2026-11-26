

'''calificacion = float*(input("Calificación: "))

if calificacion >= 6:
    print("Aprobado")
else:
    print("Reprobado")


a) Si la calificación es 9 o más, diga "Excelente"
b) Si es menor que 0 o mayor de 10, diga "Calificación inválida"
c) Si es mayor que 8 pero menor de 9, diga "Buen trabajo"'''

#va

calificacion = float(input("Calificación: "))


if calificacion < 0 or calificacion > 10:
    print("Calificación inválida")
elif calificacion >= 9:
    print("Excelente.")
elif calificacion >= 8:
    print("Buen trabajo.")
elif calificacion >= 7:
    print("Aprobado.")
else:
    print("Reprobado.")