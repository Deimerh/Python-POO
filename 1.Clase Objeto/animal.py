class Animales:
    
    #creamos metodo constructor
    def __init__(self, nombre, lugar, habitad, años):
        self.nombre = nombre
        self.lugar = lugar
        self.habitad = habitad
        self.años = años
        
    def  mostrar(self):
        print("Informacion de los animales ")
        print("Nombre: "+self.nombre)
        print("Lugar: "+self.lugar)
        print("Habitad: "+self.habitad)
        print("Años: "+self.años)
        print("-----------------------------------")
            
    #validar que animal es carnivoro
    
    def carnivoro(self):
        #elemento privado llamdado carne
        self.carne = str(input("El animal es un Felino? "))
        #evalumos si es o no es
        if self.carne == "si":
            print("El animal: "+self.nombre+ " es carnivoro")
        else:
             print("El animal: "+self.nombre+ " no es carnivoro")
             
    def hierva(self):
        #elemento privado llamdado carne
        self.hierva = str(input("El animal es un hervivoro? "))
        #evalumos si es o no es
        if self.hierva == "si":
            print("El animal: "+self.nombre+ " es hervivoro")
        else:
             print("El animal: "+self.nombre+ " no es hervivoro")
               
#creamos animales
animal1 = Animales("Gato", "Domestico", "Zona Verde", "2 años")
animal2 = Animales("Erizo", "Zona rocosas", "Bosques", "5 años")
animal3 = Animales("Cerdo", "Domestica", "Humedos, frios, soleados", "6 años")

#mostrar datos de animales
animal1.mostrar()
animal2.mostrar()
animal3.mostrar()
animal1.carnivoro()
animal2.hierva()