from claseConjunto import conjunto
def carga(k):
     listaa = []
     centinela = True
     while centinela:
         n = int(input(f"Ingrese numero a cargar en el conjunto {k+1}, finalice con 0: "))
         if(n == 0):
            centinela = False
         else:   
            listaa.append(n)
     return listaa

def menu(listaO):
    print("-----MENU-----")
    op = int(input("1_ Union de dos conjuntos \n2_ Diferencia de dos conjuntos \n3_ Verificar igualdad entre conjuntos \n4_EXIT\n"))

    if(op == 1):
        print(f"La lista resultante de la union de dos conjuntos es: {listaO[0]+listaO[1]}")
    elif(op==2):
        print(f"La diferencia de los elementos del conjunto 1 con el conjunto 2 es: {listaO[0]-listaO[1]}")
    elif(op==3):
        Boleano = (listaO[0] == listaO[1])
        if Boleano == True:
            print(f"Las listas son iguales")
        else: 
            print("Las listas son diferentes")
    else:
        exit
    