from Pedido import Pedido


class GestionPedido:
    def __init__(self)->None:
        self.pedidos:list [Pedido]= []

    def crear_pedido(self)->Pedido:
        pedido = Pedido()
        self.pedidos.append(pedido)
        return pedido

    def cancelar_pedido(self, pedido:Pedido)->None:
        if pedido in self.pedidos:
            self.pedidos.remove(pedido)

    def visualizar_pedidos(self)->None:
        for pedido in self.pedidos:
            print(f"pedido {pedido.productos} - Estado: {pedido.estado} ")
