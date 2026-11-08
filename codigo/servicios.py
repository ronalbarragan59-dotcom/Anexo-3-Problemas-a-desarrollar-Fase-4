
from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, precio, cantidad_de_tiempo):
        self.nombre = nombre 
        self.precio = precio
        self.cantidad_de_tiempo = cantidad_de_tiempo
 
    @abstractmethod
    def calcular_costos(self):
        pass
    
    @abstractmethod
    def describir_servicios(self):
        pass
    
    @abstractmethod
    def validar_parametros(self):
        pass
    
#CLASES HIJAS

class ReservaSala(Servicio):
    def __init__(self, nombre, precio, cantidad_de_tiempo, espacio_de_la_sala):
        super().__init__(nombre, precio, cantidad_de_tiempo)
        self.espacio_de_la_sala = espacio_de_la_sala 
        
    def calcular_costos(self):
        return self.precio * self.cantidad_de_tiempo 
    
    def describir_servicios(self):
        return (f"nombre: {self.nombre} | Espacio: {self.espacio_de_la_sala} | Costo: {self.calcular_costos()}")
    
    def validar_parametros(self):
        if self.precio <= 0 or self.cantidad_de_tiempo <=0 or not self.espacio_de_la_sala or self.espacio_de_la_sala.strip()=="":
            return False
        return True 
        

class AlquilerDeEquipos(Servicio):
    def __init__(self, nombre, precio, cantidad_de_tiempo, nombre_del_equipo):
        super().__init__(nombre, precio, cantidad_de_tiempo)
        self.nombre_del_equipo = nombre_del_equipo
        
    def calcular_costos(self):
        return self.precio * self.cantidad_de_tiempo
    
    def describir_servicios(self):
        return (f"nombre: {self.nombre} | Nombre del equipo:{self.nombre_del_equipo} | Costo: {self.calcular_costos()}")
    
    def validar_parametros(self):
        if self.precio <=0 or self.cantidad_de_tiempo <= 0 or not self.nombre_del_equipo or self.nombre_del_equipo.strip()=="":
            return False
        return True
    
class AsesoriaPersonalizada(Servicio):
    def __init__(self, nombre, precio, cantidad_de_tiempo, modalidad_de_asesoria, costo_adicional):
        super().__init__(nombre, precio, cantidad_de_tiempo)
        self.modalidad_de_asesoria = modalidad_de_asesoria
        self.costo_adicional = costo_adicional
        
    def calcular_costos(self):
    #Si la modalidad llega a ser presencial usamos .lower() para evitar los errores de los usuarios por si lo llegan a escribir en mayuscula o minuscula
         if self.modalidad_de_asesoria.strip().lower =="presencial":
        #Aca se define la operacion o la tarifa para saber la difereancia de la asesoria presencial 
            return (self.precio * self.cantidad_de_tiempo) + self.costo_adicional
         else:
            return self.precio * self.cantidad_de_tiempo 
    
    def describir_servicios(self):
        return (f"nombre: {self.nombre} | Modalidad de la asesoria: {self.modalidad_de_asesoria} | Costo:{self.calcular_costos()}")
    
    def validar_parametros(self):
        if self.precio <=0 or self.cantidad_de_tiempo <=0 or self.costo_adicional <0 or not self.modalidad_de_asesoria or self.modalidad_de_asesoria.strip()=="": 
            return False
        return True
    
    
