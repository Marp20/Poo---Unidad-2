class PlanAhorro:
    __codigo = 0
    __modelo = ''
    __version = ''
    __valor = 0.0
    __cuotas = 0
    __cuotaspagas= 0

    def __init__(self, codigo, modelo, version, valor, cuotas, cutoaspagas):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
        self.__cuotas = cuotas
        self.__cuotaspagas = cutoaspagas
    
    def get_codigo(self):
        return int(self.__codigo)
    
    def get_modelo(self):
        return str(self.__modelo)
    
    def get_version(self):
        return str(self.__version)
    
    def get_valor(self):
        return int(self.__valor)
    
    def get_cuotas(self):
        return int(self.__cuotas)
    
    def get_cuotaspagas(self):
        return int(self.__cuotaspagas)
    
    def set_valor(self,precio):
        self.__valor = precio
        return None
    
    def set_cuotaspagas(self,mod):
        self.__cuotaspagas = mod
        return None
    
    def get_valorCuotas(self):
        valor = float((self.__valor/self.__cuotas)+self.__valor*0.10)
        return valor