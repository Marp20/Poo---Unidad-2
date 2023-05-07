class ViajeroFrec:
    __numViajero: int
    __dni: str
    __nom: str
    __apellido: str
    __millasAcum: int

    def __init__ (self, numViajero=None, dni=None, nombre=None, apellido=None, millasAcum=0):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__nom = nombre
        self.__apellido = apellido
        self.__millasAcum = millasAcum

    def __eq__ (self, n):
        # print("millas viajero actual {}, millas ingresadas {}".format(self.__millasAcum,n))
        if self.__millasAcum == n:
            r=True
        else: 
            r=False
            
        return r
    
    def __req__(self,n):
        # print("millas viajero actual {}, millas ingresadas {}".format(self.__millasAcum,n))
        if self.__millasAcum == n:
            r=True
        else:
            r=False
        return r
    
        
    def __radd__ (self, n):
        return ViajeroFrec(self.__numViajero, self.__dni, self.__nom, self.__apellido, self.__millasAcum + n)
    
    def __rsub__ (self, n):
        return ViajeroFrec(self.__numViajero, self.__dni, self.__nom, self.__apellido, self.__millasAcum - n)

    def cantidadTotalDeMillas (self):
        return self.__millasAcum
    
    def acumularMillas (self, xMillas):
        self.__millasAcum += xMillas
        return self.__millasAcum

    def canjearMillas (self, xMillas):
        if xMillas <= self.__millasAcum:
            self.__millasAcum -= xMillas
        else:
            print('Error, cantidad de millas insuficiente')
        return self.__millasAcum
    
    def getNumero(self):
        return int (self.__numViajero)
    
    def getMillas (self):
        return self.__millasAcum
    
    def getNombre(self):
        return self.__nom
    
    def getApellido(self):
        return self.__apellido