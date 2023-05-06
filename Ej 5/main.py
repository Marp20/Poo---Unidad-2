from PlanAhorro import PlanAhorro 
from menu import menu
import csv

if __name__ == '__main__':
    lista= []
    archivo = open('planes.csv')
    reader = csv.reader(archivo, delimiter = ';')
    next(reader)

    for fila in reader:
        row =int(fila[0])
        row1 =str(fila[1])
        row2 =str(fila[2])
        row3 =float(fila[3])
        row4 =int(fila[4])
        row5 =int(fila[5])
        plan = PlanAhorro(row,row1,row2,row3,row4,row5)
        lista.append(plan)
    menu(lista)