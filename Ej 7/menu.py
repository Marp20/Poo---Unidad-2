from claseViajeroFrec import ViajeroFrec

def menu(lista):
    print('Ingrese una opcion.\n  1#_Comprar millas\n  2#_Acumular Millas.\n  3#_Canjear Millas.\n')
    opcion = input('Ingrese opcion: ')
    if opcion == '1':
        valor = int(input('Ingrese millas a comparar '))
        for instancia in lista:
            if instancia == valor and valor == instancia:
                print(f'Cantidad de millas iguales para viajero: {instancia.getNumero()}')
            else:
                print(f'Las millas no coinciden para vaijero: {instancia.getNumero()}')
                
    elif opcion == '2':
        numviajero = int(input('Ingresar numero de viajero: '))
        band =True
        for instancia in lista:
            if instancia.getNumero() == numviajero:
                instancia = 100+instancia
                band = False
                print('Se acumularon millas exitosamente.\n Cantidad total de milla: ',instancia.cantidadTotalDeMillas())
        if band == True:
            print('No se encontro viajero') 
    
    elif opcion == '3':
        numviajero = int(input('Ingresar numero de viajero: '))
        band =True
        for instancia in lista:
            if instancia.getNumero() == numviajero:
                instancia = 100-instancia
                band = False
                print('Se canjearon millas exitosamente.\n Cantidad total de millas: ',instancia.cantidadTotalDeMillas())
        if band == True:
            print('No se encontro viajero')          
                 