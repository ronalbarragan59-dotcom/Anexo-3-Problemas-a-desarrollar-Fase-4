
from clientes import Cliente
from servicios import Servicio
from excepciones import ErrorReserva


class Reserva:
    def __init__(self, cliente, servicio, duracion):

        if not isinstance(cliente, Cliente):
            raise ErrorReserva("El cliente ingresado no es valido")

        if not isinstance(servicio, Servicio):
            raise ErrorReserva("El servicio ingresado no es valido")

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorReserva("La duracion debe ser mayor que cero")

        if not servicio.validar_parametros():
            raise ErrorReserva("Los parametros del servicio no son validos")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"

    def ConfirmarEstadoDeLaReserva(self):
        if self.estado != "pendiente":
            raise ErrorReserva("La reserva no se puede confirmar en su estado actual")

        self.estado = "Confirmada"

    def CancelacionDeLaReserva(self):
        if self.estado == "Cancelada":
            raise ErrorReserva("La reserva ya se encuentra cancelada")

        if self.estado == "Procesada":
            raise ErrorReserva("No se puede cancelar una reserva procesada")

        self.estado = "Cancelada"

    def ProcesarReserva(self):
        if self.estado != "Confirmada":
            raise ErrorReserva("La reserva debe estar confirmada para procesarse")

        self.estado = "Procesada"
