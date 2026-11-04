
from abc import ABC, abstractmethod

# Clase general para las entidades del sistema
class Entidad(ABC):

    def __init__(self, identificacion):
        self._identificacion = identificacion

    # Metodo para mostrar la informacion de cada entidad
    @abstractmethod
    def mostrar_informacion(self):
        pass
