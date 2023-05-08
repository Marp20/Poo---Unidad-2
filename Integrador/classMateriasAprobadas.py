class materiasA:
    __dni =''
    __nombre = ''
    __fecha = ''
    __nota = 0.0
    __aprobacion = ''
    
    def __init__(self,dni='',nombre='',fecha='',nota=0.0,aprobacion=''):
        self.__dni = dni
        self.__fecha = fecha
        self.__nombre = nombre
        self.__nota = nota
        self.__aprobacion = aprobacion
    
    def getDni(self):
        return self.__dni
    
    def getNota(self):
        return self.__nota
    
    def getNombre(self):
        return self.__nombre
    
    def getAprobacion(self):
        return self.__aprobacion