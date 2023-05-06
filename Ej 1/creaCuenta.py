from classEmail import Email

def creaCuenta(direccion):
    parts = direccion.split('@')
    idCuenta = parts[0]
    parts = parts[1].split('.')
    Dom = parts[0]
    TipoDom = parts[1]
    Passw = input('ingrese contrasena: ')
    email = Email(idCuenta, Dom, TipoDom, Passw)
    return email