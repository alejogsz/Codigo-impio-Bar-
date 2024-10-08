from Usuario import Usuario
 
class Administrador(Usuario):
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)

    def ver_mesas(self, gestion_mesas):
        print(f"{self.nombre} puede ver todas las mesas del bar:")
        gestion_mesas.visualizar_mesas()

    def ver_propinas_meseros(self, meseros):
        print(f"Propinas de los meseros vistas por {self.nombre}:")
        for mesero in meseros:
            print(f"{mesero.nombre}: {mesero.propinas}")

    def ver_pedidos(self, gestion_pedidos):
        print(f"{self.nombre} revisa todos los pedidos:")
        gestion_pedidos.visualizar_pedido()

   
