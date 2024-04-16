from abc import ABC, abstractmethod


class Componente(ABC):
    @abstractmethod
    def mostrar(self):
        pass


class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(f"  - Pieza: {self.nombre}")


class Subconjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar_componente(self, componente):
        self.componentes.append(componente)

    def mostrar(self):
        print(f"Subconjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar()


pieza1 = Pieza("Pieza 1")
pieza2 = Pieza("Pieza 2")
pieza3 = Pieza("Pieza 3")
pieza4 = Pieza("Pieza 4")


subconjunto1 = Subconjunto("Subconjunto 1")
subconjunto1.agregar_componente(pieza1)
subconjunto1.agregar_componente(pieza2)
subconjunto1.agregar_componente(pieza3)
subconjunto1.agregar_componente(pieza4)

subconjunto2 = Subconjunto("Subconjunto 2")
subconjunto2.agregar_componente(Pieza("Pieza 5"))
subconjunto2.agregar_componente(Pieza("Pieza 6"))
subconjunto2.agregar_componente(Pieza("Pieza 7"))
subconjunto2.agregar_componente(Pieza("Pieza 8"))

subconjunto3 = Subconjunto("Subconjunto 3")
subconjunto3.agregar_componente(Pieza("Pieza 9"))
subconjunto3.agregar_componente(Pieza("Pieza 10"))
subconjunto3.agregar_componente(Pieza("Pieza 11"))
subconjunto3.agregar_componente(Pieza("Pieza 12"))


print("Subconjuntos existentes:")
subconjunto1.mostrar()
subconjunto2.mostrar()
subconjunto3.mostrar()


subconjunto_opcional = Subconjunto("Subconjunto Opcional")
subconjunto_opcional.agregar_componente(Pieza("Pieza 13"))
subconjunto_opcional.agregar_componente(Pieza("Pieza 14"))
subconjunto_opcional.agregar_componente(Pieza("Pieza 15"))
subconjunto_opcional.agregar_componente(Pieza("Pieza 16"))


print("\nSubconjunto opcional adicional:")
subconjunto_opcional.mostrar()

