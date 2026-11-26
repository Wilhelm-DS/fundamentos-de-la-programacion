class Vehiculo:
    def __init__(self, marca, modelo, fecha, color):
        self.marca = marca
        self.modelo = modelo
        self.fecha = fecha
        self.color = color

    def mostrar_caracteristicas(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Fecha: {self.fecha}")
        print(f"Color: {self.color}")