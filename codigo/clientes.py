
# Importamos la clase Entidad
from entidades import Entidad


# Clase Cliente que hereda de Entidad
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        # Inicializamos la identificacion heredada
        super().__init__(identificacion)

        # Validamos que los datos no esten vacios
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")

        if not correo.strip() or "@" not in correo:
            raise ValueError("El correo electronico no es valido")

        if not telefono.isdigit() or len(telefono) < 7:
            raise ValueError("El telefono debe tener minimo 7 digitos")

        # Guardamos los datos de forma privada
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Metodo para mostrar la informacion del cliente
    def mostrar_informacion(self):
        print("Identificacion:", self._identificacion)
        print("Nombre:", self.__nombre)
        print("Correo:", self.__correo)
        print("Telefono:", self.__telefono)
