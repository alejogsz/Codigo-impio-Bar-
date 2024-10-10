from IMesa import IMesa
from Pedido import Pedido

class Mesa:
    def __init__(self, id:int)->None:
        self.id:int = id
        self.estado:str = 'Disponible'
        self.pedidos:list[Pedido] = []

    def agregar_pedido(self, pedido:Pedido)->None:
        self.pedidos.append(pedido)
        self.estado:str = 'Ocupada'

    def calcular_total(self)->int:
        return sum(pedido.calcular_total() for pedido in self.pedidos)

    def cambiar_estado(self, estado:str)->None:
        self.estado:str = estado
