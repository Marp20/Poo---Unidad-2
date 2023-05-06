from classEmail import Email
from devuelveEmail import Suscripcion
from PasswordChange import cambia
from creaCuentaCsv import opencsv
from buscarPorDominio import busqueda


if __name__=='__main__':
    idCuenta = input('ingresar Id: ')
    Dom = input('ingresar dominio: ')
    tipoDom = input('ingresar Tipo de dominio: ')
    Passw = input('ingresar Password: ')
    email = Email(idCuenta,Dom,tipoDom,Passw)
    print(email)
    Suscripcion(email)
    email = Email(idCuenta,Dom,tipoDom, Passw=cambia(Passw))
    direccion = input('Crear cuenta: \n ingrese Correo deseado: ')
    email = Email.creaCuenta(direccion) 
    print(email)
    email_lista = []
    archivo = input('Ingrese nombre del achivo: ') 
    email_lista = opencsv(archivo)
    busqueda(archivo)