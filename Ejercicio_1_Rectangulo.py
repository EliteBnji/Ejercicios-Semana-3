class Rectangulo:
    def __init__(self, ancho,largo):
        self.ancho = ancho
        self.largo = largo

    def calcularArea(self):
        return (self.largo * self.ancho)

    def calcularPerimetro(self):
        return 2 * (self.largo + self.ancho)

    def cambiarLargo(self, nuevo_largo):
        self.largo = nuevo_largo

    def cambiarAncho(self, nuevo_ancho):
        self.ancho = nuevo_ancho


#Uso
rectangulo1 = Rectangulo(4, 6)

print("El area del rectangulo es:", rectangulo1.calcularArea())
print("El perímetro del rectangulo es:", rectangulo1.calcularPerimetro())

#Cambio
rectangulo1.cambiarAncho(10)
rectangulo1.cambiarLargo(15)

print("El nuevo area del rectangulo es:", rectangulo1.calcularArea())
print("El nuevo perimetro del rectangulo es:", rectangulo1.calcularPerimetro())


