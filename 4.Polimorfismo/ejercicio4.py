# Clase padre InstrumentoMusical
class InstrumentoMusical:
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo

    def tocar(self):
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print("------------------------------------")


# Clase Guitarra que hereda de InstrumentoMusical
class Guitarra(InstrumentoMusical):
    def __init__(self, marca, tipo, numero_cuerdas, amplificador):
        super().__init__(marca, tipo)
        self.numero_cuerdas = numero_cuerdas
        self.amplificador = amplificador

    def tocar(self):
        print("------------------------------------")
        print("¡Tocando la Guitarra!")
        print("------------------------------------")
        super().tocar()  # Llama al método tocar de la clase padre
        print(f"Número de cuerdas: {self.numero_cuerdas}")
        print(f"Amplificador: {self.amplificador}")
        print("------------------------------------")


# Clase Piano que hereda de InstrumentoMusical
class Piano(InstrumentoMusical):
    def __init__(self, marca, tipo, numero_teclas, tipo_mecanismo):
        super().__init__(marca, tipo)
        self.numero_teclas = numero_teclas
        self.tipo_mecanismo = tipo_mecanismo

    def tocar(self):
        print("------------------------------------")
        print("¡Tocando el Piano!")
        print("------------------------------------")
        super().tocar()  # Llama al método tocar de la clase padre
        print(f"Número de teclas: {self.numero_teclas}")
        print(f"Tipo de mecanismo: {self.tipo_mecanismo}")
        print("------------------------------------")


# Clase Trompeta que hereda de InstrumentoMusical
class Trompeta(InstrumentoMusical):
    def __init__(self, marca, tipo, material, rango_tonal):
        super().__init__(marca, tipo)
        self.material = material
        self.rango_tonal = rango_tonal

    def tocar(self):
        print("------------------------------------")
        print("¡Tocando la Trompeta!")
        print("------------------------------------")
        super().tocar()  # Llama al método tocar de la clase padre
        print(f"Material: {self.material}")
        print(f"Rango tonal: {self.rango_tonal}")
        print("------------------------------------")


# Función que muestra la información de cualquier tipo de instrumento musical
def tocar_instrumento(instrumento):
    instrumento.tocar()


# Instancias de cada clase
guitarra = Guitarra("Fender", "Eléctrica", 6, "Marshall")
piano = Piano("Yamaha", "Acústico", 88, "Mecánico")
trompeta = Trompeta("Bach", "De viento", "Latón", "Do-Sol")

# Llamado al método tocar para cada instrumento
tocar_instrumento(guitarra)
tocar_instrumento(piano)
tocar_instrumento(trompeta)
