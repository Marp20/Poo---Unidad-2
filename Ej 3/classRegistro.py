class Registro:
    __temp = 0
    __presion = 0
    __presion = 0
    def __init__(self, temp, hum, presion):
        self.__temp = temp
        self.__hum = hum
        self.__presion= presion

    def get_temp(self):
        return self.__temp
    
    def get_hum(self):
        return self.__hum
    
    def get_presion(self):
        return self.__presion