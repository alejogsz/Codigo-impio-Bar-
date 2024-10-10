from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre: str, password: any)->None:
        self.nombre:str = nombre

    def autenticar(self, password: str) -> bool:
        return self.password == password
