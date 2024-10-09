# Clase padre Profesion
class Profesion:
    def __init__(self, nombre, campo):
        self.nombre = nombre
        self.campo = campo

    def trabajar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Campo de trabajo: {self.campo}")
        print("------------------------------------")


# Clase Medico que hereda de Profesion
class Medico(Profesion):
    def __init__(self, nombre, campo, especialidad, hospital):
        super().__init__(nombre, campo)
        self.especialidad = especialidad
        self.hospital = hospital

    def trabajar(self):
        print("------------------------------------")
        print("¡Información del Médico!")
        print("------------------------------------")
        super().trabajar()  # Llama al método trabajar de la clase padre
        print(f"Especialidad: {self.especialidad}")
        print(f"Hospital: {self.hospital}")
        print("------------------------------------")


# Clase Ingeniero que hereda de Profesion
class Ingeniero(Profesion):
    def __init__(self, nombre, campo, especializacion, proyectos_actuales):
        super().__init__(nombre, campo)
        self.especializacion = especializacion
        self.proyectos_actuales = proyectos_actuales

    def trabajar(self):
        print("------------------------------------")
        print("¡Información del Ingeniero!")
        print("------------------------------------")
        super().trabajar()  # Llama al método trabajar de la clase padre
        print(f"Especialización: {self.especializacion}")
        print(f"Proyectos actuales: {self.proyectos_actuales}")
        print("------------------------------------")


# Clase Docente que hereda de Profesion
class Docente(Profesion):
    def __init__(self, nombre, campo, asignatura, institucion):
        super().__init__(nombre, campo)
        self.asignatura = asignatura
        self.institucion = institucion

    def trabajar(self):
        print("------------------------------------")
        print("¡Información del Docente!")
        print("------------------------------------")
        super().trabajar()  # Llama al método trabajar de la clase padre
        print(f"Asignatura: {self.asignatura}")
        print(f"Institución: {self.institucion}")
        print("------------------------------------")


# Función que muestra la información de cualquier tipo de objeto Profesion
def descripcion_profesional(profesion):
    profesion.trabajar()


# Instancias de cada clase
medico = Medico("Dr. Juan Pérez", "Salud", "Cardiología", "Hospital Central")
ingeniero = Ingeniero("Ana Martínez", "Construcción", "Ingeniería Civil", "Puente Metropolitano")
docente = Docente("Luis Gómez", "Educación", "Matemáticas", "Escuela Secundaria Nacional")

# Llamado al método trabajar para cada profesional
descripcion_profesional(medico)
descripcion_profesional(ingeniero)
descripcion_profesional(docente)
