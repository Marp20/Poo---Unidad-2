from classAlumnos import Alumno
from classMateriasAprobadas import materiasA
from manejador import materiasA
import numpy as np
import os

os.system('cls' if os.name == 'nt' else 'clear')

def menu(lista,array):
    print(' Bienvendio al menu de opciones.\n  1#_Promedio y aplazos de un alumno.\n  2#_Alumno que aprobaron promocional.\n  3#_Lista de alumnoes\n')
    opcion = input('Ingresar Opcion: ')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if opcion == '1':
        cont=0
        nota=0.0
        dni = input('Ingresar dni del alumno.\n     ')
        for fila in lista:
            if dni == fila.getDni():
                cont+=1
                nota=nota+int(fila.getNota())
        if nota != 0:
            print(f'El alumno con dni {dni} tiene un promedio de {nota/cont}')
        else:
            print('El alumno no ha sido cargado o no ha rendido ninguna materia')   
    
    elif opcion == '2':
        array.alumnos_aprobados(lista)
    
    elif opcion == '3':
        array.alumnos_ordenados()