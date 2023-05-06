if __name__ == '__main__':
    from claseConjunto import conjunto
    from funciones import carga
    from funciones import menu
    listaObj = []
    #i = int(input("Ingrese la cantidad de conjuntos a cargar: "))
    for k in range(2):
        lista = carga(k)
        nuevoObjeto = conjunto(lista)
        listaObj.append(nuevoObjeto)
    
    menu(listaObj)
    
    
    
