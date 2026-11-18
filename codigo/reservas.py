
from clientes import Cliente
from servicios import Servicio
from excepciones import ErrorReserva


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if not isinstance(cliente, Cliente):
            raise ErrorReserva("El cliente ingresado no es valido")

        if not isinstance(servicio, Servicio):
            raise ErrorReserva("El servicio ingresado no es valido")

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ErrorReserva("La duracion debe ser mayor que cero")

        if not servicio.validar_parametros():
            raise ErrorReserva("Los parametros del servicio no son validos")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"

    # Metodo para confirmar la reserva
    def ConfirmarEstadoDeLaReserva(self):

        if self.estado != "pendiente":
            raise ErrorReserva(
                "La reserva no se puede confirmar en su estado actual"
            )

        self.estado = "Confirmada"

    # Metodo para cancelar la reserva
    def CancelacionDeLaReserva(self):

        if self.estado not in ("pendiente", "Confirmada"):
            raise ErrorReserva(
                "La reserva no se puede cancelar en su estado actual"
            )

        self.estado = "Cancelada"

    # Metodo para procesar la reserva
    def ProcesarReserva(self):

        if self.estado != "Confirmada":
            raise ErrorReserva(
                "La reserva debe estar confirmada para procesarse"
            )

        self.estado = "Procesada"
