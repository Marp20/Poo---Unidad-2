from classEmail import Email

def cambia(Passw):
    aPassw = input('ingresar contrasena actual: ')
    if  Passw == aPassw:
        nPassw = input('ingresar contrasena nueva: ')
    else:
        print('error')
    return nPassw