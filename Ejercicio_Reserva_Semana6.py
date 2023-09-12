class Reserva:
    def __init__ (self, nombre_del_pasajero, numero_de_vuelo, fecha):
        self.nombre_del_pasajero = nombre_del_pasajero
        self.numero_de_vuelo = numero_de_vuelo
        self.fecha = fecha
    
class ReservaEconomica(Reserva):
    def __init__ (self, nombre_del_pasajero, numero_de_vuelo, fecha, equipaje_economico):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.equipaje_economico = equipaje_economico

    def mostrar_detalle(self):
        print("Detalles de la reserva:", self.nombre_del_pasajero, self.numero_de_vuelo, self.fecha, self.equipaje_economico)


class ReservaBusiness(Reserva):
    def __init__ (self, nombre_del_pasajero, numero_de_vuelo, fecha, equipaje_business):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.equipaje_business = equipaje_business

    def mostrar_detalle(self):
        print("Detalles de la reserva:", self.nombre_del_pasajero, self.numero_de_vuelo, self.fecha, self.equipaje_business)
    

class ReservaPrimeraClase(Reserva):
    def __init__ (self, nombre_del_pasajero, numero_de_vuelo, fecha, equipaje_primeraclase):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.equipaje_primeraclase = equipaje_primeraclase


    def mostrar_detalle(self):
        print("Detalles de la reserva:", self.nombre_del_pasajero, self.numero_de_vuelo, self.fecha, self.equipaje_primeraclase)
    


reserva1 = ReservaEconomica("Jorge", 34, "20-05-2024", "Equipaje de Mano")
reserva1.mostrar_detalle()

reserva2 = ReservaBusiness("Yé", 25, "07-09-2023", "Equipaje de Mano y Maleta")
reserva2.mostrar_detalle()

reserva3 = ReservaPrimeraClase("Daniel", 22, "19-12-2023", "Asiento de Lujo, Pantalla Interactiva,Equipaje de Mano y Maleta")
reserva3.mostrar_detalle()
