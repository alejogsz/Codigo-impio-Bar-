from Factura import Factura
from GestionPedido import GestionPedido
from Mesa import Mesa
from Pedido import Pedido
from Usuario import Usuario
from GestionMesas import GestionDeMesas

class Mesero(Usuario):
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        self.pedidos_atendidos:list[Pedido] = []
        self.propinas:int = 0
        self.mesas_asignadas = []

    def registrar_pedido(self, mesa:Mesa, pedido:Pedido)->None:
        if mesa in self.mesas_asignadas:
             mesa.agregar_pedido(pedido)
             self.pedidos_atendidos.append(pedido)
        else:
            print("No puedes registrar un pedido en esta mesa. No está asignada.")


    def liquidar_factura(self, pedido:Pedido, propina:int)->None:
        factura = Factura(pedido, propina)
        self.propinas += factura.calcular_propina()
        factura.liquidar()

  def ver_pedidos(self, gestion_pedidos:GestionPedido):
        print(f"{self.nombre} puede ver todos los pedidos del bar:")
        gestion_pedidos.visualizar_pedidos()
