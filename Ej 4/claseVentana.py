class Ventana:
    __titulo = ''
    __xvsi = 0
    __yvsi = 0
    __xvid = 0
    __yvid = 0
   
    def __init__(self, titulo, xvsi=0, yvsi=0, xvid=500, yvid=500):
        if (xvsi < xvid and yvsi < yvid):
            self.__titulo = titulo
            self.__xvsi = xvsi
            self.__yvsi = yvsi
            self.__xvid = xvid
            self.__yvid = yvid
        else:
            print("Datos erroneos, no se pudo crear el objeto")
    
    def mostrar(self):
        print(f'Titulo: {self.__titulo} Vertice Superior Izquierdo: ({self.__xvsi}, {self.__yvsi}) Vertice Inferior Derecho: ({self.__xvid}, {self.__yvid})')
        
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return self.__xvid - self.__xvsi
    def ancho(self):
        return self.__yvid - self.__yvsi
    def moverDerecha(self, cantidad = 1):
        if self.__xvid + cantidad <= 500:
            self.__xvsi += cantidad
            self.__xvid +=cantidad
        else:
            print(f"No se puede mover {self.__titulo} {cantidad} a la derecha")
    def moverIzquierda(self, cantidad = 1):
        if self.__xvsi - cantidad >= 0:
            self.__xvsi -= cantidad
            self.__xvid -= cantidad
        else:
            print(f"No se puede mover la ventana {self.__titulo} {cantidad} a la izquierda")
    def bajar(self, cantidad = 1):
        if self.__yvid + cantidad <= 500: 
            self.__yvsi += cantidad
            self.__yvid += cantidad
        else:
            print(f"No se puede bajar {cantidad} la ventana {self.__titulo}")
            
    def subir(self, cantidad = 1):
        if self.__yvsi - cantidad >= 0:
                self.__yvsi -= cantidad
                self.__yvid -= cantidad
        else:
            print(f"No se puede subir {cantidad} la ventana {self.__titulo}")
            