class Celular:
    #metodo constructor
    def __init__(self, nombre, marca, imei, almacenamiento):
        self.nombre = nombre
        self.marca = marca
        self.imei = imei
        self.almacenamiento = almacenamiento
    #metodos para mostrar detalles del celular
    def mostrar_detalles(self):
        print("Informacion del celular ")
        print("Nombre " + self.nombre)
        print("Marca " + self.marca)
        print("Imei " + self.imei)
        print("Almacenamiento " + self.almacenamiento)
        print("--------------------------------------")

#metodo para encender el celular
    def encender(self):
    #definfir el atributo privado energia para encender
        self.energia = int(input("Digite el valor de la carga "))
    #evaluamos si tiene carga
        if self.energia > 0:
            print("El celular "+self.nombre+" se puede encender")
        else:
            print("El celular "+self.nombre+" no se puede encender")

          
# creamos los celulares
celular1 = Celular("Samsung Galaxy S23", "SAMSUNG", "1231464323", "256GB")
celular2 = Celular("Iphone 15", "Apple", "2165373138","128GB")
celular3 = Celular("Motorola Edge 40 Pro", "Motorola", "32442352354", "256GB")

#mostrar los detalles de cada celular
celular1.mostrar_detalles()
celular1.encender()
celular2.mostrar_detalles()
celular3.mostrar_detalles()