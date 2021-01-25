class Animales:
    def __init__(self, nombre, edad, salud, felicidad): #nombre, una edad, un nivel de salud y un nivel de felicidad.
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad

    def Display_info(self):
        print(self.nombre, self.salud, self.felicidad)

    def Alimentacion(self):
        self.salud += 10
        self.felicidad += 10


class Leon(Animales):
    def __init__(self, nombre, edad, salud=30, felicidad=20, peso=175):

        super().__init__(nombre, edad, salud, felicidad)
        self.peso = peso


    def Alimentacion(self):
        self.salud += 15
        self.felicidad += 10


class Tigre(Animales):
    def __init__(self, nombre, edad, salud=25, felicidad=10):
        super().__init__(nombre, edad, salud, felicidad)


    def Alimentacion(self):
        self.salud += 20
        self.felicidad += 15


class Oso(Animales):
    def __init__(self, nombre, edad, salud=50, felicidad=15, pelaje=2):
        super().__init__(nombre, edad, salud, felicidad)
        self.pelaje = pelaje


    def Alimentacion(self):
        self.salud += 30
        self.felicidad += 20

class Zoo:
    def __init__(self, nombrezoo):
        self.nombrezoo = nombrezoo
        self.animales = []

    def add_leon(self, nombre, edad):
        leon = Leon(nombre, edad)
        self.animales.append(leon)

    def add_tigre(self, nombre, edad):
        tigre = Tigre(nombre, edad)
        self.animales.append(tigre)

    def add_oso(self, nombre, edad):
        oso = Oso(nombre, edad)
        self.animales.append(oso)

    def print_all_info(self):
        for animal in self.animales:
            animal.display_info()