
# Importamos las clases necesarias
from clientes import Cliente
from servicios import Servicio
from reservas import Reserva
from registros import RegistroSistema
from excepciones import ErrorServicio, ErrorReserva


class SistemaGestion:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []
        self.registro = RegistroSistema()

    # Metodo para registrar clientes
    def registrar_cliente(self, cliente):

        try:
            if not isinstance(cliente, Cliente):
                raise TypeError("El dato ingresado no es un cliente valido")

            for cliente_guardado in self.clientes:
                if cliente_guardado._identificacion == cliente._identificacion:
                    raise ValueError("Ya existe un cliente con esa identificacion")

            self.clientes.append(cliente)
            self.registro.guardar_evento(
                "Cliente registrado: " + cliente._identificacion
            )

            print("Cliente agregado al sistema correctamente")

        except (ValueError, TypeError) as error:
            self.registro.guardar_error(str(error))
            raise

    # Metodo para consultar clientes
    def consultar_clientes(self):

        if len(self.clientes) == 0:
            print("No hay clientes registrados")
        else:
            print("\nLista de clientes registrados:")

            for cliente in self.clientes:
                cliente.mostrar_informacion()
                print("------------------------")

    # Metodo para registrar servicios
    def registrar_servicio(self, servicio):

        try:
            if not isinstance(servicio, Servicio):
                raise ErrorServicio("El dato ingresado no es un servicio valido")

            if not servicio.validar_parametros():
                raise ErrorServicio("Los datos del servicio no son validos")

            self.servicios.append(servicio)

            self.registro.guardar_evento(
                "Servicio registrado: " + servicio.nombre
            )

            print("Servicio agregado al sistema correctamente")

        except ErrorServicio as error:
            self.registro.guardar_error(str(error))
            raise

    # Metodo para consultar servicios
    def consultar_servicios(self):

        if len(self.servicios) == 0:
            print("No hay servicios registrados")
        else:
            print("\nLista de servicios registrados:")

            for servicio in self.servicios:
                print(servicio.describir_servicios())
                print("------------------------")

    # Metodo para registrar reservas
    def registrar_reserva(self, reserva):

        try:
            if not isinstance(reserva, Reserva):
                raise ErrorReserva("El dato ingresado no es una reserva valida")

            if reserva.cliente not in self.clientes:
                raise ErrorReserva("El cliente no se encuentra registrado")

            if reserva.servicio not in self.servicios:
                raise ErrorReserva("El servicio no se encuentra registrado")

            self.reservas.append(reserva)

            self.registro.guardar_evento(
                "Reserva registrada para el cliente: "
                + reserva.cliente._identificacion
            )

            print("Reserva agregada al sistema correctamente")

        except ErrorReserva as error:
            self.registro.guardar_error(str(error))
            raise

    # Metodo para consultar reservas
    def consultar_reservas(self):

        if len(self.reservas) == 0:
            print("No hay reservas registradas")
        else:
            print("\nLista de reservas registradas:")

            for reserva in self.reservas:
                print("Cliente:", reserva.cliente._identificacion)
                print("Servicio:", reserva.servicio.nombre)
                print("Duracion:", reserva.duracion)
                print("Estado:", reserva.estado)
                print("------------------------")
