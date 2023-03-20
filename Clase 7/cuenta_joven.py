#Ejercicio 8

from persona import Persona
from cuenta import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad = 0.0,bonificacion = 0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = float(bonificacion)
        
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, value):
        self.__bonificacion = float(value)
        
    def es_titular_valido(self):
        if self.__titular.es_mayor_de_edad() and self.__tituar.edad <= 25:
            return True
        else:
            return False
    
    def mostrar(self):
        super().mostrar()
        print ("Cuenta Joven bonificacion:" + str(self.__bonificacion))
    
    
p = Persona("Amalia", 45, 23643079)
#p.mostrar()
c = CuentaJoven(p, 50.0, "a25.0")
c.mostrar()   
        
