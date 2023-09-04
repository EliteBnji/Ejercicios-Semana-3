
pi = 3.14
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return pi * (self.radio**2)

    def calcularPerimetro(self):
        return (2 * pi )* self.radio

    def cambiarRadio(self, nuevo_radio):
        self.radio = nuevo_radio 

#Uso
circulo1 = Circulo(5)


print("El área del circulo es:", circulo1.calcularArea())
print("Perímetro del circulo:", circulo1.calcularPerimetro())

#Cambio de Radio
circulo1.cambiarRadio(7)
print("El área del circulo nuevo es:", circulo1.calcularArea())

