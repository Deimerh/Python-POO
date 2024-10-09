'''
Animales con Polimorfismo
Crea tres clases: Perro, Gato, y Pájaro, cada una con un método sonido() que haga el sonido correspondiente.
'''
# Clase padre Animal
class Animal:
    def __init__(self, raza, edad):
        self.raza = raza
        self.edad = edad

    def mostrar_info(self):
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print("------------------------------------")


# Clase Perro hereda de Animal
class Perro(Animal):
    def __init__(self, raza, edad, registro_medico, tamaño):
        super().__init__(raza, edad)
        self.registro_medico = registro_medico
        self.tamaño = tamaño
        self.domestico = input("¿Tu canino está domesticado? ")

    def mostrar_info(self):
        print("------------------------------------")
        print("¡Firulais!")
        print("------------------------------------")
        super().mostrar_info()  # Llama al método mostrar_info de la clase padre
        print(f"Registro médico: {self.registro_medico}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Domesticado: {self.domestico}")
        print("------------------------------------")


# Clase Gato hereda de Animal
class Gato(Animal):
    def __init__(self, raza, edad, especie):
        super().__init__(raza, edad)
        self.especie = especie

    def mostrar_info(self):
        print("¡Miauu!")
        print("------------------------------------")
        super().mostrar_info()  # Llama al método mostrar_info de la clase padre
        print(f"Especie: {self.especie}")
        print("------------------------------------")


# Clase Pajaro hereda de Animal
class Pajaro(Animal):
    def __init__(self, especie, habitad, alimento):
        super().__init__(especie, "Desconocida")  # Usamos especie como raza en la clase padre
        self.habitad = habitad
        self.alimento = alimento

    def mostrar_info(self):
        print("Información del ave")
        print("------------------------------------")
        super().mostrar_info()  # Llama al método mostrar_info de la clase padre
        print(f"Habitad: {self.habitad}")
        print(f"Alimento: {self.alimento}")
        print("------------------------------------")


# Función que muestra la información de cualquier tipo de objeto Animal
def descripcion(animal):
    animal.mostrar_info()


# Instancias de cada clase
perro = Perro("Pastor Alemán", 5, "12345ABC", "Grande")
gato = Gato("Siames", 3, "Felino")
pajaro = Pajaro("Canario", "Bosques", "Semillas")

# Llamado al método mostrar_info para cada objeto
descripcion(perro)
descripcion(gato)
descripcion(pajaro)

