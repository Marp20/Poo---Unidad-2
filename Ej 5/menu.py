from PlanAhorro import PlanAhorro

def menu(lista):
        
        opcion = input('Ingrese una opcion.\n 1# Calcular valor de cuota.\n 2# Buscar por presupuesto.\n 3# Monto para licitar.\n 4# Modificar cuotas a licitar.\n')

        if opcion == '1':
            for plan in lista:
                print(f'Codigo: {plan.get_codigo()}.\nModelo: {plan.get_modelo()}.\nVersion del vehiculo: {plan.get_version()}')
                precio = float(input('Ingresar precio actual: '))
                plan.set_valor(precio)
         
        elif opcion == '2':
              precio = float(input('Ingrese presupuesto: '))
              for plan in lista:
                valor = plan.get_valorCuotas()
                if precio < valor:
                    print(f'Codigo: {plan.get_codigo()}.\nModelo: {plan.get_modelo()}.\nVersion del vehiculo: {plan.get_version()}')

        elif opcion == '3':
            for plan in lista:
                valor = plan.get_valorCuotas()
                print(f'Para licitar vehiculo se necesita pagar el monto de: {plan.get_cuotaspagas() * valor}')  

        elif opcion == '4':
            codigo = int(input('Ingresar codigo'))
            for plan in lista:
                if codigo == lista[0]:
                    mod = int(input('Ingresar cantidad cuotas pagas para licitar'))
                    plan.set_cuotaspagas(mod)
        