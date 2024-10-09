from Producto import Producto
from Mesa import Mesa
from Mesero import Mesero
from Administrador import Administrador
from GestionMesas import GestionDeMesas
from GestionPedido import GestionPedido


def main():
    # Crear productos disponibles en el bar
    cerveza = Producto("Cerveza", 3.0)
    pizza = Producto("Pizza", 8.0)

    # Crear gestión de mesas
    gestion_mesas = GestionDeMesas()

    # Crear mesas
    mesa1 = Mesa(1)
    mesa2 = Mesa(2)
    mesa3 = Mesa(3)

    # Agregar mesas a la gestión
    gestion_mesas.agregar_mesa(mesa1)
    gestion_mesas.agregar_mesa(mesa2)
    gestion_mesas.agregar_mesa(mesa3)

    # Crear meseros
    mesero1 = Mesero("Carlos")
    mesero2 = Mesero("Ana")

    # Asignar mesas a los meseros
    mesero1.mesas_asignadas.append(mesa1)
    mesero2.mesas_asignadas.append(mesa2)

    # Crear administrador
    admin = Administrador("Luis")

    # Crear gestión de pedidos
    gestion_pedidos = GestionPedido()

    # Ciclo para interacción continua
    while True:
        print("\n=== Bienvenido al Bar ===")
        print("1. Acceder como Mesero")
        print("2. Acceder como Administrador")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nSelecciona un Mesero:")
            print("1. Carlos")
            print("2. Ana")
            mesero_opcion = input("Seleccione el mesero: ")

            if mesero_opcion == "1":
                mesero_actual = mesero1
            elif mesero_opcion == "2":
                mesero_actual = mesero2
            else:
                print("Mesero no válido.")
                continue

            while True:
                print(f"\n=== Mesero {mesero_actual.nombre} ===")
                print("1. Ver mesas asignadas")
                print("2. Registrar pedido en una mesa")
                print("3. Liquidar factura de un pedido")
                print("4. Volver al menú principal")
                mesero_accion = input("Seleccione una acción: ")

                if mesero_accion == "1":
                    mesero_actual.ver_mesas(gestion_mesas)

                elif mesero_accion == "2":
                    mesa_id = int(input("Ingrese el ID de la mesa para registrar el pedido: "))
                    cantidad_cerveza = int(input("Cantidad de cervezas: "))
                    cantidad_pizza = int(input("Cantidad de pizzas: "))

                    # Encontrar la mesa
                    mesa = None
                    for m in mesero_actual.mesas_asignadas:
                        if m.id == mesa_id:
                            mesa = m
                            break

                    if mesa is None:
                        print("No tienes asignada esa mesa.")
                        continue

                    # Crear un nuevo pedido
                    pedido = gestion_pedidos.crear_pedido()
                    pedido.agregar_producto(cerveza, cantidad_cerveza)
                    pedido.agregar_producto(pizza, cantidad_pizza)

                    # Registrar pedido
                    mesero_actual.registrar_pedido(mesa, pedido)
                    print(f"Pedido registrado en la mesa {mesa_id}.")

                elif mesero_accion == "3":
                    mesa_id = int(input("Ingrese el ID de la mesa para liquidar la factura: "))
                    propina = int(input("Ingrese el porcentaje de propina: "))

                    # Encontrar la mesa
                    mesa = None
                    for m in mesero_actual.mesas_asignadas:
                        if m.id == mesa_id:
                            mesa = m
                            break

                    if mesa is None:
                        print("No tienes asignada esa mesa.")
                        continue

                    # Liquidar factura del último pedido de la mesa
                    if mesa.pedidos:
                        ultimo_pedido = mesa.pedidos[-1]
                        mesero_actual.liquidar_factura(ultimo_pedido, propina)
                        print(f"Factura liquidada para la mesa {mesa_id}.")
                    else:
                        print(f"La mesa {mesa_id} no tiene pedidos pendientes.")

                elif mesero_accion == "4":
                    break

                else:
                    print("Opción no válida.")

        elif opcion == "2":
            while True:
                print(f"\n=== Administrador {admin.nombre} ===")
                print("1. Ver todas las mesas")
                print("2. Ver propinas de meseros")
                print("3. Volver al menú principal")
                admin_accion = input("Seleccione una acción: ")

                if admin_accion == "1":
                    admin.ver_mesas(gestion_mesas)

                elif admin_accion == "2":
                    admin.ver_propinas_meseros([mesero1, mesero2])

                elif admin_accion == "3":
                    break

                else:
                    print("Opción no válida.")

        elif opcion == "3":
            print("Gracias por utilizar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "_main_":
    main()
