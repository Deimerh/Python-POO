from abc import ABC, abstractmethod
 
class Tareaempleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass
    
class Ingeniero(Tareaempleado):
     def __init__(self, tarea1):
         self.tarea1 = tarea1
         
     def realizar_tarea(self):
         return self.tarea1 * 8
     
class Doctor(Tareaempleado):
    def __init__(self, citas):
        self.citas = citas
        
    def realizar_tarea(self):
        return self.citas * 5
    
    
#uso de clases
Ingeniero = Ingeniero(3)
print(f"Cantidad de tareas realizadas por el ingeniero: {Ingeniero.realizar_tarea()}")


Doctor = Doctor(4)
print(f"Cantiadad de tareas realizadas por el Doctor:  {Doctor.realizar_tarea()}")