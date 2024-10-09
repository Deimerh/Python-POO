class Moto:
    #metodo constructor
    def __init__(self, nombre, modelo, velocidad_final, torque):
        self.nombre = nombre
        self.modelo = modelo
        self.velocidad_final = velocidad_final
        self.torque = torque
        
        
    def mostrar(self):
        print("Informacion de Motocicletas")
        print("Nombre: "+self.nombre)
        print("Modelo: "+self.modelo)
        print("Velocidad Final: "+self.velocidad_final)
        print("Torque: "+self.torque)
        print("----------------------------------------------")
    
 #creamos las motocicletas
moto1 = Moto("Boxer CT 100", "2020", "95KM/h", "8.0 NM")
moto2 = Moto("Yamaha XTZ 250", "2023", "143KM/h", "14 NM")
moto3 = Moto("BMW S1000RR", "2021", "310KM/h", "41 NM")


#llamar metodos
moto1.mostrar()
moto2.mostrar()
moto3.mostrar()
