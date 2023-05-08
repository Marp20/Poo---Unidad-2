class Alumno:
    __dni = ''
    __apellido = ''
    __nombre = ''
    __carrera = ''
    __aniocursa = ''
    
    def __init__(self,dni='',apellido='',nombre='',carrera='',aniocursa=''):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__aniocursa = aniocursa
        
    def getAnio(self):
        return self.__aniocursa
    
    def getDni(self):
        return self.__dni
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getCarrera(self):
        return self.__carrera
    
    def __gt__(self,otro):
        if self.__apellido < otro:
            r = True
        else:
            r = False
        return r
    
    def __rgt__(self,otro):
        if self.__apellido < otro:
            r = True
        else:
            r = False
        return r
    
    