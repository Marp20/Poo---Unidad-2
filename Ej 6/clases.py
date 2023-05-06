class Viajero:
    __numeroviajero=0
    __dni=""
    __nombre=""
    __apellido=""
    __millasacum=0

    def __init__(self,num,dni,nom,ap,millas):
        self.__numeroviajero=num
        self.__dni=dni
        self.__nombre=nom
        self.__apellido=ap
        self.__millasacum=millas
    def getnum(self):
        return self.__numeroviajero
    def getdoc(self):
        return self.__dni
    def getnom(self):
        return self.__nombre
    def getap(self):
        return self.__apellido
    def getmillas(self):
        return self.__millasacum
    def __eq__(self,otro):
        print("millas viajero actual{}, millas ingresadas{}".format(self.__millasacum,otro))
        if self.__millasacum == otro:  
            r=True
        else:
            r=False
        return r
    def __req__(self,otro):
        print("millas viajero actual{}, millas ingresadas{}".format(self.__millasacum,otro))
        if self.__millasacum == otro:  
            r=True
        else:
            r=False
        return r
    def __radd__(self,otro):
        return Viajero(self.__numeroviajero,self.__dni,self.__nombre,self.__apellido,self.__millasacum + otro)
    def __rsub__(self,otro):
        return Viajero(self.__numeroviajero,self.__dni,self.__nombre,self.__apellido,self.__millasacum - otro)