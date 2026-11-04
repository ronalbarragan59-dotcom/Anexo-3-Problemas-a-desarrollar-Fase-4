# Importamos las clases necesarias
from entidades import Entidad
from excepciones import ErrorCliente


# Clase Cliente que hereda de Entidad
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        super().__init__(identificacion)

        # Validamos los datos del cliente
        if not nombre.strip():
            raise ErrorCliente("El nombre no puede estar vacio")

        if not correo.strip() or "@" not in correo:
            raise ErrorCliente("El correo electronico no es valido")

        if not telefono.isdigit() or len(telefono) < 7:
            raise ErrorCliente("El telefono debe tener minimo 7 digitos")

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Metodo para mostrar la informacion
    def mostrar_informacion(self):
        print("Identificacion:", self._identificacion)
        print("Nombre:", self.__nombre)
        print("Correo:", self.__correo)
        print("Telefono:", self.__telefono)
