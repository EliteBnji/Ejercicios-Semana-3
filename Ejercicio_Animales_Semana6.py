class Animal:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def Sonido(self):
    print("Guau!")

class Perro(Animal):
  pass

class Gato(Animal):
  def Sonido(self):
    print("Miau!")

class Pajaro(Animal):
  def Sonido(self):
    print("Cru Cru")

perro1 = Perro("Pepe", 4) 
gato1 = Gato("Batman", 3) 
pajaro1 = Pajaro("Luffy",2) 

for x in (perro1, gato1, pajaro1):
  print(x.nombre)
  print(x.edad)
  x.Sonido()
