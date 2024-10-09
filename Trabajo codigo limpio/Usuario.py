from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre: str)->None:
        self.nombre:str = nombre
