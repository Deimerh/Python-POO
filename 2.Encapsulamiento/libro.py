#iniciamos clase
class Libros:
    #constructor
    def __init__(self, titulo, autor, isbn, editorial):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.editorial = editorial
    
    #metodo getter
    def obtener_titulo(self):
        return self.__titulo
    
    def obtener_autor(self):
        return self.__autor
    
    def obtener_isbn(self):
        return self.__isbn
    
    #metodod setter
    def nuevo_titulo(self, new_titulo):
        self.__titulo = new_titulo
        
    def nuevo_autor(self, new_autor):
        self.__autor = new_autor
    
    def nuevo_isbn(self, new_isbn):
        self.__isbn = new_isbn
    
    #mostrar detalles
    
    def mostrar(self):
        print(f"Titulo: { self.__titulo} ")
        print(f"Autor: { self.__autor }")
        print(f"ISBN: {self.__isbn }")
        print(f"Editorial: { self.editorial }")
        
#objeto
libro = Libros("100 Años de soledad", "Gabriel Garcia Marquez",  9788497592208, "Editorial Sudamericana")

#imprimir 
libro.mostrar()
print("--------------------------------")
#imprimir el atributo encapsulado
libro.nuevo_titulo("Don Quijote de la Mancha")
print(f"Titulo: { libro.obtener_titulo() }")
libro.nuevo_autor("Miguel de cervantes Saavedra")
print(f"Autor: { libro.obtener_autor() }")
libro.nuevo_isbn(9789583004445)
print(f"ISBN: {libro.obtener_isbn() }")
print(f"Editorial: {libro.editorial}")