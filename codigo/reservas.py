
class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"
    
    def ConfirmarEstadoDeLaReserva(self):
        self.estado = "Confirmada"
        
    def CancelacionDeLaReserva(self):
        if self.estado == "Cancelada":
            raise Exception("La reserva ya se encuentra cancelada y ya no se puede volver a modificar")
        else:
            self.estado = "Cancelada"
        

    
    
    
    
