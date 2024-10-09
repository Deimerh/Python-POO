from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    
class Cuadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_area(self):
        return self.lado **2
    
class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        self.radio
    
    def calcular_area(self):
        return math.pi * (self.radio **2)
        
        
        
#uso de las clases
Cuadrado = Cuadrado(5)
print(f"Area del cuadrado: {Cuadrado.calcular_area()}")

Circulo = Circulo(3)
print(f"Area del circulo: {Circulo.calcular_area()}")