#Ejercicio 7

from persona import Persona

class Cuenta:
    def __init__(self, titular, cantidad = 0.0):
        self.__titular = titular
        self.__cantidad = float(cantidad)
        
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @titular.setter
    def titular(self, value):
        self.__titular = value
        
    @cantidad.setter
    def cantidad(self, value):
        self.__cantidad = float(value)
        
    def mostrar(self):
        self.__titular.mostrar()
        print ("cantidad:" + str(self.__cantidad))
        
    def ingresar(self, cantidad):
        cantidad = float(cantidad)
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
            
    def retirar(self, cantidad):
        cantidad = float(cantidad)
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad
        
        
#p = Persona("Amalia", 45, 23643079)
#p.mostrar()
#c = Cuenta(p, "a50.0")
#c.mostrar()