class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def ladrar(self):
        return "¡Guau!"

miPerro = Perro("Firulais")
print(miPerro.ladrar())