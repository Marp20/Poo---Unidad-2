from classViajeroF import ViajeroF
from Display import display_viajeros
import sys
import csv

if __name__ == '__main__':
    viajeros = []
    with open('Viajeros.csv') as archivo:
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            viajero = ViajeroF(int(fila[0]), (fila[1]), (fila[2]), (fila[3]), int(fila[4]))
            viajeros.append(viajero)
    display_viajeros(viajeros)
    num = int(input())
    for k in range(len(viajeros)):
     if  viajeros[k].get_numero() == num:
        buscado = viajeros[k]
        print("Se ha encontrado al viajero ")
        print("1: Consultar cantidad de millas ")
        print("2: Acumular millas ")
        print("3: Canjear Millas")
        print("0: salir")
        opcion = int(input("Opcion: "))
        if opcion == 1:
                print(f"La cantidad de millas son: {buscado.cantidadTotaldeMillas()}")
        elif opcion == 2:
                acummm = int(input("Ingrese la cantidad de millas a acumular"))
                buscado.acumularMillas(acummm)
        elif opcion == 3:
                masmillas = int(input("ingrese la cantidad de millas a canjear "))
                buscado.canjearMillas(masmillas)
        elif opcion == 0:
                exit()
        else: print("ERROR, ingresaste mal el numero")
    k=0
    while k < len(viajeros):
        print(f"El objeto de el viajero {viajeros[k].get_numero()} llamado {viajeros[k].get_nombre()} ocupa {sys.getsizeof(viajeros[k])} bytes de memoria")
        k+=1
    
    