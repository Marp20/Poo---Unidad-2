class Email:
    __idCuenta = ''
    __Dom = ''
    __TipoDom = ''
    __Passw = ''
    def __init__(self, idCuenta, Dom, TipoDom, Passw):
        self.__idCuenta = idCuenta
        self.__Dom = Dom
        self.__TipoDom = TipoDom
        self.__Passw = Passw
    def __str__(self):
        return self.__idCuenta+'@'+self.__Dom+'.'+self.__TipoDom
    def __repr__(self):
        return f"Email: '{print(self)} '"
    def getDominio(self):
        return self.__Dom
    def setPassw(self, nPassw):
        self.__Passw = nPassw
    def getPassw(self):
        return self.__Passw
    def creaCuenta(dir):
        parts = dir.split('@')
        idCuenta = parts[0]
        parts = parts[1].split('.')
        Dom = parts[0]
        TipoDom = parts[1]
        Passw = input('ingrese contrasena: ')
        email = Email(idCuenta, Dom, TipoDom, Passw)
        return email