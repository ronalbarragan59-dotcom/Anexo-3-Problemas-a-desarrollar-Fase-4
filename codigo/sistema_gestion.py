# Importamos la clase Cliente
from clientes import Cliente


# Clase para administrar el sistema
class SistemaGestion:

    def __init__(self):
        self.clientes = []

    # Metodo para registrar clientes
    def registrar_cliente(self, cliente):

        if not isinstance(cliente, Cliente):
            raise TypeError("El dato ingresado no es un cliente valido")

        for cliente_guardado in self.clientes:
            if cliente_guardado._identificacion == cliente._identificacion:
                raise ValueError("Ya existe un cliente con esa identificacion")

        self.clientes.append(cliente)
        print("Cliente agregado al sistema correctamente")

    # Metodo para consultar clientes
    def consultar_clientes(self):

        if len(self.clientes) == 0:
            print("No hay clientes registrados")
        else:
            print("\nLista de clientes registrados:")

            for cliente in self.clientes:
                cliente.mostrar_informacion()
                print("------------------------")
