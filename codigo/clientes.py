
# Importamos las clases necesarias
from entidades import Entidad
from excepciones import ErrorCliente


# Clase Cliente que hereda de Entidad
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        super().__init__(identificacion)

        # Validamos que los datos sean textos
        if not isinstance(identificacion, str):
            raise ErrorCliente("La identificacion debe ser un texto")

        if not isinstance(nombre, str):
            raise ErrorCliente("El nombre debe ser un texto")

        if not isinstance(correo, str):
            raise ErrorCliente("El correo debe ser un texto")

        if not isinstance(telefono, str):
            raise ErrorCliente("El telefono debe ser un texto")

        # Validamos la identificacion
        if not identificacion.strip() or not identificacion.isdigit():
            raise ErrorCliente("La identificacion debe contener solo numeros")

        # Validamos el nombre
        if not nombre.strip():
            raise ErrorCliente("El nombre no puede estar vacio")

        # Validamos el correo
        if (
            not correo.strip()
            or " " in correo
            or "@" not in correo
            or "." not in correo.split("@")[-1]
        ):
            raise ErrorCliente("El correo electronico no es valido")

        # Validamos el telefono
        if not telefono.isdigit() or len(telefono) < 7 or len(telefono) > 10:
            raise ErrorCliente("El telefono debe tener entre 7 y 10 digitos")

        # Guardamos los datos personales
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Metodo para mostrar la informacion
    def mostrar_informacion(self):
        print("Identificacion:", self._identificacion)
        print("Nombre:", self.__nombre)
        print("Correo:", self.__correo)
        print("Telefono:", self.__telefono)
