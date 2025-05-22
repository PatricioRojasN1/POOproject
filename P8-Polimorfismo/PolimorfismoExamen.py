class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido genérico")


class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")


class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

def hacer_sonidos(animales):
    for animal in animales:
        animal.hacer_sonido()

animales = [
    Animal("Animal genérico"),
    Perro("Rex"),
    Gato("Silvestre"),
    Perro("Max"),
    Gato("Luna")
]

hacer_sonidos(animales) 