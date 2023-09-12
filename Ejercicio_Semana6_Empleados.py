class Empleado:
    def __init__ (self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    
class Gerente(Empleado):
    def __init__ (self, nombre, edad , salario, aptitud):
        super().__init__(nombre, edad, salario)
        self.aptitud = aptitud

    def describir_rol(self):
        print("Detalles Rol de Gerente: ", self.nombre, self.edad, self.salario, self.aptitud)


class Ingeniero(Empleado):
    def __init__ (self, nombre, edad , salario, especializacion):
        super().__init__(nombre, edad, salario)
        self.especializacion = especializacion

    def describir_rol(self):
        print("Detalles Rol de Ingeniero: ", self.nombre, self.edad, self.salario, self.especializacion)
    

class Asistente(Empleado):
    def __init__ (self, nombre, edad, salario, tipo):
        super().__init__(nombre, edad, salario)
        self.tipo = tipo

    def describir_rol(self):
        print("Detalles Rol de Asistente: ", self.nombre, self.edad, self.salario, self.tipo)
    

gerente1 = Gerente("Martin", 34, "$100000", "Actitud Positiva" )
gerente1.describir_rol()

ingeniero1 = Ingeniero("Nicolas", 27, "$30000", "AereoEspacial")
ingeniero1.describir_rol()

asistene1 = Asistente("Byron", 24, "$40000", "Virtual")
asistene1.describir_rol()
