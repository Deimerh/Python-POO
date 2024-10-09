from abc import ABC, abstractmethod
 
class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass
    
class EmpleadotieompoCompleto(Empleado):
     def __init__(self, tiempo):
         self.tiempo = tiempo
         
     def calcular_salario(self):
         return self.tiempo *20000
     
class EmpleadoporHoras(Empleado):
    def __init__(self, horas):
        self.horas = horas
        
    def calcular_salario(self):
        return self.horas * 5000
    
    
#uso de clases
EmpleadotieompoCompleto = EmpleadotieompoCompleto(3)
print(f"Salario por tiempo completo: {EmpleadotieompoCompleto.calcular_salario()}")


EmpleadoporHoras = EmpleadoporHoras(5)
print(f"Salario por horas: {EmpleadoporHoras.calcular_salario()}")