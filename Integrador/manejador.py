import numpy as np
from classAlumnos import Alumno
from classMateriasAprobadas import materiasA

class ManejadorAlumnos:
    def __init__(self):
        self.alumnos = np.array([], dtype=Alumno)
    
    def agregar_alumno(self, alumno):
        self.alumnos = np.append(self.alumnos, alumno)
        
    def alumnos_aprobados(self,lista):
        bool = False
        materia = input('Ingresar nombre de materia (un error de tipeo concluira con el programa): ')
        for fila in lista:
            if fila.getNombre() == materia:
                for index, value in enumerate(self.alumnos):
                    if self.alumnos[index].getDni() == fila.getDni() and fila.getAprobacion() == 'P':
                        if bool == False:
                            print('   Dni        Apellido y Nombre     Nota      Anio que cursa')
                            bool = True
                        print(f'{fila.getDni()}        {self.alumnos[index].getApellido()} {self.alumnos[index].getNombre()}      {fila.getNota()}           {self.alumnos[index].getAnio()}')
    
    def alumnos_ordenados(self):
        sorted_alumnos = self.alumnos[np.argsort([Alumno.getAnio() for Alumno in self.alumnos])]
        
        for i, fila in enumerate(sorted_alumnos):
            a = 1
            h = len(sorted_alumnos)-1
            if i != h:
                g=i+1
                if sorted_alumnos[i].getAnio() and int(sorted_alumnos[i].getAnio()) == a:
                    if sorted_alumnos[i].getAnio() == sorted_alumnos[g].getAnio() and sorted_alumnos[g].getApellido() < sorted_alumnos[i].getApellido():
                        aux = Alumno(sorted_alumnos[i])
                        sorted_alumnos[i] = sorted_alumnos[g]
                        sorted_alumnos[g] = Alumno(aux)
                else:
                    a+=1
                    
                    
        for i, fila in enumerate(sorted_alumnos):
            print(sorted_alumnos[i].getDni(), sorted_alumnos[i].getApellido(), sorted_alumnos[i].getNombre(), sorted_alumnos[i].getCarrera(), sorted_alumnos[i].getAnio())