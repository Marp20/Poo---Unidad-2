from menu import menu
from claseViajeroFrec import ViajeroFrec
import os
import csv

os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    listaViaj = []
    archivo = open('Viajeros.csv')
    reader = csv.reader(archivo, delimiter=',')
    next(archivo)
    for fila in reader:
        lista = ViajeroFrec(int(fila[0]),str(fila[1]),str(fila[2]),str(fila[3]),int(fila[4]))
        listaViaj.append(lista)
    
    menu(listaViaj)
    