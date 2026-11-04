from datetime import datetime


# Clase para guardar los registros del sistema
class RegistroSistema:

    def __init__(self):
        self.archivo = "registros_sistema.txt"

    # Metodo para guardar un evento
    def guardar_evento(self, mensaje):

        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open(self.archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"[{fecha}] EVENTO: {mensaje}\n")

    # Metodo para guardar un error
    def guardar_error(self, mensaje):

        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open(self.archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"[{fecha}] ERROR: {mensaje}\n")
