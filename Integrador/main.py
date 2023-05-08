from classAlumnos import Alumno
from classMateriasAprobadas import materiasA
from manejador import ManejadorAlumnos
from menu import menu
import numpy as np
import csv

if __name__ == '__main__':
   
    archivoAl = open('alumnos.csv')
    reader = csv.reader(archivoAl, delimiter=';')
    next(archivoAl)
    arrayAl = ManejadorAlumnos()
    for fila in reader:
        alumno = Alumno(str(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), int(fila[4]))
        arrayAl.agregar_alumno(alumno)

    
    archivoMat = open('materiasAprobadas.csv')
    readerMat = csv.reader(archivoMat, delimiter=';')
    next(archivoMat) 
    
    listaMat = []
    
    for fila in readerMat:
        materia = materiasA(str(fila[0]),str(fila[1]),str(fila[2]),float(fila[3]),str(fila[4]))
        listaMat.append(materia)
    archivoMat.close()

    menu(listaMat,arrayAl)
    