#Ejercicio 6

class Persona:
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = int(edad)
        self.__dni = int(dni)
        
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
        
    @edad.setter
    def edad(self, value):
        self.__edad = int(value)
        
    @dni.setter
    def dni(self, value):
        self.__dni = int(value)
        
    def mostrar(self):
        print ("nombre:"+self.__nombre+" edad:"+str(self.__edad)+" dni:"+str(self.__dni))
        
    def es_mayor_de_edad(self):
        if self.__edad >= 18:
            return True
        else:
            return False        
        
#p = Persona("Amalia", "h56", "h23643079")
#p.mostrar()

