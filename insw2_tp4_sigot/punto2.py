from abc import ABC, abstractmethod

# Implementación del patrón Bridge

class TrenLaminador(ABC):
    @abstractmethod
    def producir_lamina(self, ancho):
        pass

class TrenLaminador5Metros(TrenLaminador):
    def producir_lamina(self, ancho):
        print(f"Produciendo lámina de {ancho} metros de ancho en el tren laminador de 5 metros")

class TrenLaminador10Metros(TrenLaminador):
    def producir_lamina(self, ancho):
        print(f"Produciendo lámina de {ancho} metros de ancho en el tren laminador de 10 metros")

# Abstracción del patrón Bridge

class Lamina:
    def __init__(self, espesor, tren_laminador):
        self.espesor = espesor
        self.tren_laminador = tren_laminador

    def enviar_a_producir(self, ancho):
        self.tren_laminador.producir_lamina(ancho)

# Uso del patrón Bridge

lamina = Lamina(0.5, TrenLaminador5Metros())
lamina.enviar_a_producir(5)

lamina = Lamina(0.5, TrenLaminador10Metros())
lamina.enviar_a_producir(10)
