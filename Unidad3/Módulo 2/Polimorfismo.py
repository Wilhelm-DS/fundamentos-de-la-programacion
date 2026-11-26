import math

class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * math.pow(self.radio, 2)

class Rectangulo(Figura):
    def __init__(self, base, altura):   
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2    

Figuras = [Rectangulo(5, 10), Circulo(7), Triangulo(6, 5)]

for figura in Figuras:
    print(type(figura).__name__, "Área:", round(figura.area(), 2))