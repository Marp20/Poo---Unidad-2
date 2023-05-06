from classRegistro import Registro

def menu(registros_mensuales):
    cont = 0
    acumtemp = 0
    tempMax = 0
    tempmin = 111111111
    print('Ingrese alguna de las siguientes opciones:\n1# Mostrar datos\n2# Temperatura promedio\n3# Mostrar datos por/h')
    opcion = input()
    
    if opcion == "1":
        for d, registros_diarios in enumerate(registros_mensuales):
            for h, registro in enumerate(registros_diarios):
                if registro is not None:
                    tempAux = registro.get_temp()
                    if tempAux > tempMax:
                        tempMax = tempAux
                        diaMax = d
                        horaMax = h
                    if tempAux < tempmin:
                        tempmin = tempAux
                        diamin = d
                        horamin = h
        print(f'El dia {diamin}, hora {horamin} hicieron {tempmin}º de temperatura minima')
        print(f'El dia {diaMax}, hora {horaMax} hicieron {tempMax}º de temperatura maxima')

    elif opcion == "2":
        hora = int(input('Ingresar hora del dia: '))
        for d, registros_diarios in enumerate(registros_mensuales):
            registro = registros_diarios[hora]
            if registro is not None:
                cont += 1
                Temp = int(registro.get_temp())
                acumtemp = acumtemp + Temp
        if cont > 0:
            prom = acumtemp / cont
            print('La temperatura promedio mensual de la hora',hora,'es',prom)
        else:
            print('No hay registros en esa hora')

    elif opcion == "3":
        condicion = 0
        dia = int(input('Ingresar dia a mostrar:'))
        registros_diarios = registros_mensuales[dia]
        for h, registro in enumerate(registros_diarios):
            if registro is not None:
                if condicion == 0:
                    print('Hora      Temperatura      Humedad      Presion')
                    condicion = 1
                print(f'{h}            {registro.get_temp()}             {registro.get_hum()}           {registro.get_presion()}')
            