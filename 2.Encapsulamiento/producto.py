#creamos la clase
class Productos:
    #iniciamos constructor
    def  __init__(self, nombre, precio, cantidad, categoria):
        self.__nombre = nombre
        self.__precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
        
    #metodo getter
    def obtenernombre(self):
        return self.__nombre
    
    def obtenerprecio(self):
        return self.__precio
    
    #metodo setter
    def modificarnombre(self, newName):
        self.__nombre = newName
    def modificarprecio(self, newPrecio):
        self.__precio = newPrecio
    
    #mostrar detalles
    def mostrardetalles(self):
        print("-------------------------------")
        print(f"Nombre: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Cantidad: { self.cantidad}")
        print(f"Categoria: {self.categoria}")
        print("-------------------------------")
    
#objeto
producto = Productos("Samsung Galaxi S23",3500000,2,"Tecnologia")

#imprimir
producto.mostrardetalles()


print("---------------------")

#imprimir el atributo encapsulado modificado su acceso con getter y setter
producto.modificarnombre("iphone") #setter
print(f"Nombre: { producto.obtenernombre() }") #getter
producto.modificarprecio(8676777) #setter
producto.modificarprecio(f"Precio: { producto.obtenerprecio() }") #getter
print(f"Cantidad: { producto.cantidad }")
print(f"Categoria: { producto.categoria}")