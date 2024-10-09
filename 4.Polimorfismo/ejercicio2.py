'''
Clases de  Vehículos con Polimorfismo
Crea tres clases: Carro, Moto y Bicicleta, cada una con un método descripcion() que describa el tipo de vehículo.
'''
# Clase padre Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print("------------------------------------")


# Clase Carro que hereda de Vehiculo
class Carro(Vehiculo):
    def __init__(self, marca, modelo, placa, fabricador):
        super().__init__(marca, modelo)
        self.placa = placa
        self.fabricador = fabricador

    def mostrar_informacion(self):
        print("------------------------------------")
        print("En hora buena!!! conoce el tipo de coche")
        print("------------------------------------")
        super().mostrar_informacion()  # Llama al método mostrar_informacion de la clase padre
        print(f"Placa: {self.placa}")
        print(f"Fabricador: {self.fabricador}")
        print("------------------------------------")


# Clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, velocidad, torque):
        super().__init__(marca, modelo)
        self.velocidad = velocidad
        self.torque = torque

    def mostrar_informacion(self):
        print("Veamos cuál es tu moto!!!")
        print("------------------------------------")
        super().mostrar_informacion()  # Llama al método mostrar_informacion de la clase padre
        print(f"Velocidad Final: {self.velocidad}")
        print(f"Torque: {self.torque}")
        print("------------------------------------")


# Clase Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, marca, velocidad, modo_manejo, precio):
        super().__init__(marca, "Desconocido")  # Se usa "Desconocido" como modelo en la clase padre
        self.velocidad = velocidad
        self.modo_manejo = modo_manejo
        self.precio = precio

    def mostrar_informacion(self):
        print("¡Información de la bicicleta!")
        print("------------------------------------")
        super().mostrar_informacion()  # Llama al método mostrar_informacion de la clase padre
        print(f"Velocidad Alcanzada: {self.velocidad}")
        print(f"Modo de Manejo: {self.modo_manejo}")
        print(f"Precio: {self.precio}")
        print("------------------------------------")


# Función que muestra la información de cualquier tipo de objeto Vehiculo
def descripcion(vehiculo):
    vehiculo.mostrar_informacion()


# Instancias de cada clase
objeto_carro = Carro("AUDI", 2020, "234BS", "Grupo Volkswagen")
objeto_moto = Moto("YAMAHA MT 09", 2017, "265 KM/h", "48 NM")
objeto_bici = Bicicleta("Todo terreno", "50 KM/h", "Cambio", 1200000)

# Llamado al método mostrar_info para cada objeto
descripcion(objeto_carro)
descripcion(objeto_moto)
descripcion(objeto_bici)

