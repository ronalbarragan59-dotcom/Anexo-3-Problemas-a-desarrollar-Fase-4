
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
        if self.estado == "Cancelada":
            raise ErrorReserva("No se puede confirmar una reserva cancelada")

        self.estado = "Confirmada"
        
    def CancelacionDeLaReserva(self):
        if self.estado == "Cancelada":
            raise ErrorReserva("La reserva ya se encuentra cancelada y ya no se puede volver a modificar")
        else:
            self.estado = "Cancelada"
