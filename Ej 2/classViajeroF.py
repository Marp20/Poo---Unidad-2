class ViajeroF:
    __numero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0
    def __init__(self, numero, dni, nombre, apellido, millas_acum):
        self.__numero = numero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def get_numero(self):
        return self.__numero
    
    def get_dni(self):
        return self.__dni
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def cantidadTotaldeMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self, millas):
        self.__millas_acum = self.__millas_acum + millas
        print(self.__millas_acum)
        return self.__millas_acum
    
    def canjearMillas(self, canje):
        if canje < self.__millas_acum:
            self.__millas_acum = self.__millas_acum - canje
        else:
            print('Error al canjear millas, no tiene las suficientes para la operacion.')
        return self.__millas_acum
     
    def __gt__(self, otro):
        return self.__millas_acum > otro.__millas_acum
   