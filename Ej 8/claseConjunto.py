class conjunto:
    __numeros = []
    def __init__(self, listaNumeros):
        self.__numeros = listaNumeros
    def getLista(self):
        return self.__numeros
    def __add__(self, otroObjeto):
        listaRet= []
        listaFuncion = self.__numeros + otroObjeto.getLista()
        for i in range(len(listaFuncion)):
            if listaFuncion[i] not in listaRet:
                listaRet.append(listaFuncion[i])
        return listaRet
    def __sub__ (self, otroObjeto):
        listaRet= []
        for i in range(len(self.__numeros)):
            if self.__numeros[i] not in otroObjeto.getLista():
                listaRet.append(self.__numeros[i])
        return listaRet
    def __eq__(self, otroObjeto):
        listaOtroObjeto = otroObjeto.getLista()
        Valor = True
        i=0
        while Valor == True and i < len(self.__numeros):
            if self.__numeros[i] not in listaOtroObjeto:
                Valor = False
            i+=1
        while Valor == True and i < len(listaOtroObjeto):
            if listaOtroObjeto[i] not in self.__numeros:
                Valor = False
            i+=1
        return Valor