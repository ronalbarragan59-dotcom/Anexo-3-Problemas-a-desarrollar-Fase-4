
from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, precio, cantidad_de_tiempo):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un texto")

        if not isinstance(precio, (int, float)) or isinstance(precio, bool):
            raise ValueError("El precio debe ser numerico")

        if not isinstance(cantidad_de_tiempo, (int, float)) or isinstance(cantidad_de_tiempo, bool):
            raise ValueError("La cantidad de tiempo debe ser numerica")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")

        if precio <= 0 or cantidad_de_tiempo <= 0:
            raise ValueError("El precio y el tiempo deben ser mayores que cero")

        self.nombre = nombre
        self.precio = precio
        self.cantidad_de_tiempo = cantidad_de_tiempo

    def validar_costos(self, descuento, impuesto):
        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool):
            raise ValueError("El descuento debe ser numerico")

        if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool):
            raise ValueError("El impuesto debe ser numerico")

        if descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")

        if impuesto < 0:
            raise ValueError("El impuesto no puede ser negativo")

    @abstractmethod
    def calcular_costos(self, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir_servicios(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass


# CLASES HIJAS

class ReservaSala(Servicio):

    def __init__(self, nombre, precio, cantidad_de_tiempo, espacio_de_la_sala):
        super().__init__(nombre, precio, cantidad_de_tiempo)

        if not isinstance(espacio_de_la_sala, str) or not espacio_de_la_sala.strip():
            raise ValueError("El espacio de la sala no es valido")

        self.espacio_de_la_sala = espacio_de_la_sala

    def calcular_costos(self, descuento=0, impuesto=0):
        self.validar_costos(descuento, impuesto)

        costo = self.precio * self.cantidad_de_tiempo
        costo = costo - (costo * descuento / 100)
        costo = costo + (costo * impuesto / 100)
        return costo

    def describir_servicios(self):
        return f"Nombre: {self.nombre} | Espacio: {self.espacio_de_la_sala} | Costo: {self.calcular_costos()}"

    def validar_parametros(self):
        return (
            isinstance(self.nombre, str)
            and self.nombre.strip() != ""
            and self.precio > 0
            and self.cantidad_de_tiempo > 0
            and isinstance(self.espacio_de_la_sala, str)
            and self.espacio_de_la_sala.strip() != ""
        )


class AlquilerDeEquipos(Servicio):

    def __init__(self, nombre, precio, cantidad_de_tiempo, nombre_del_equipo):
        super().__init__(nombre, precio, cantidad_de_tiempo)

        if not isinstance(nombre_del_equipo, str) or not nombre_del_equipo.strip():
            raise ValueError("El nombre del equipo no es valido")

        self.nombre_del_equipo = nombre_del_equipo

    def calcular_costos(self, descuento=0, impuesto=0):
        self.validar_costos(descuento, impuesto)

        costo = self.precio * self.cantidad_de_tiempo
        costo = costo - (costo * descuento / 100)
        costo = costo + (costo * impuesto / 100)
        return costo

    def describir_servicios(self):
        return f"Nombre: {self.nombre} | Equipo: {self.nombre_del_equipo} | Costo: {self.calcular_costos()}"

    def validar_parametros(self):
        return (
            isinstance(self.nombre, str)
            and self.nombre.strip() != ""
            and self.precio > 0
            and self.cantidad_de_tiempo > 0
            and isinstance(self.nombre_del_equipo, str)
            and self.nombre_del_equipo.strip() != ""
        )


class AsesoriaPersonalizada(Servicio):

    def __init__(self, nombre, precio, cantidad_de_tiempo, modalidad_de_asesoria, costo_adicional):
        super().__init__(nombre, precio, cantidad_de_tiempo)

        if not isinstance(modalidad_de_asesoria, str) or not modalidad_de_asesoria.strip():
            raise ValueError("La modalidad de asesoria no es valida")

        if not isinstance(costo_adicional, (int, float)) or isinstance(costo_adicional, bool):
            raise ValueError("El costo adicional debe ser numerico")

        if costo_adicional < 0:
            raise ValueError("El costo adicional no puede ser negativo")

        self.modalidad_de_asesoria = modalidad_de_asesoria
        self.costo_adicional = costo_adicional

    def calcular_costos(self, descuento=0, impuesto=0):
        self.validar_costos(descuento, impuesto)

        if self.modalidad_de_asesoria.strip().lower() == "presencial":
            costo = (self.precio * self.cantidad_de_tiempo) + self.costo_adicional
        else:
            costo = self.precio * self.cantidad_de_tiempo

        costo = costo - (costo * descuento / 100)
        costo = costo + (costo * impuesto / 100)
        return costo

    def describir_servicios(self):
        return f"Nombre: {self.nombre} | Modalidad: {self.modalidad_de_asesoria} | Costo: {self.calcular_costos()}"

    def validar_parametros(self):
        return (
            isinstance(self.nombre, str)
            and self.nombre.strip() != ""
            and self.precio > 0
            and self.cantidad_de_tiempo > 0
            and isinstance(self.modalidad_de_asesoria, str)
            and self.modalidad_de_asesoria.strip() != ""
            and self.costo_adicional >= 0
        )
