class Producto:
    def __init__ (self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
class Electronico(Producto):
    def __init__ (self, nombre, precio , categoria, energia):
        super().__init__(nombre, precio, categoria)
        self.energia = energia

    def mostrar_detalle(self):
        print("Detalles del producto:", self.nombre, self.precio, self.categoria, self.energia)


class Alimenticio(Producto):
    def __init__ (self, nombre, precio , categoria, calorias):
        super().__init__(nombre, precio, categoria)
        self.calorias = calorias

    def mostrar_detalle(self):
        print("Detalles del prducto:", self.nombre, self.precio, self.categoria, self.calorias)
    

class Vestimenta(Producto):
    def __init__ (self, nombre, precio , categoria, tela):
        super().__init__(nombre, precio, categoria)
        self.tela = tela

    def mostrar_detalle(self):
        print("Detalles del prducto:", self.nombre, self.precio, self.categoria, self.tela)
    


electronico1 = Electronico("Microondas", "$10000", "Electrodomestico", "20Kw")
electronico1.mostrar_detalle()

alimenticio1 = Alimenticio("Barra de Cereal", "$400", "Snack", "1200 Calorias")
alimenticio1.mostrar_detalle()

vestimenta1 = Vestimenta("Hoddie", "$50000", "Informal", "70% Algodon")
vestimenta1.mostrar_detalle()
