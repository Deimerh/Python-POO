class Geometria:
    #metodo constructor
    def __init__(self, nombre, angulo, area, lados):
        self.nombre = nombre
        self.angulo = angulo
        self.area = area
        self.lados = lados
        
        
    def mostrar(self):
        print("Informacion de Geometria")
        print("Nombre: "+self.nombre)
        print("angulo: "+self.angulo)
        print("Area: "+self.area)
        print("lados: "+self.lados)
        print("----------------------------------------------")
    
    #evaluamos cual figura geometrica tiene mas lados
    def angulo(self):
        print("Indica cuantos lados deseas ver en la figura geomtrica (3, 8, 4)")
        self.agl = int(input("Cuantos lados deseas indicar?"))
        if self.agl == 3:
            print("La figura geometrica es un "+self.nombre)
        elif self.agl == 8:
            print("La figura geometrica es un "+self.nombre)   
        else:
            print("La figura geometrica es un Octagono")
        
 #creamos las Geometriacicletas
Geometria1 = Geometria("Triangulo", "3 angulos", "54 cm3", "3 lados")
Geometria2 = Geometria("Octagono", "8 angulos", "120 cm3", "8 lados")
Geometria3 = Geometria("Rectangulo", "4 angulos", "90 cm3", "4 lados")


#llamar metodos
Geometria1.mostrar()
Geometria2.mostrar()
Geometria3.mostrar()
Geometria1.angulo()
Geometria2.angulo()
Geometria3.angulo()