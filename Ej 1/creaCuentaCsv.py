from classEmail import Email   
import csv

def opencsv(archivo):
    email_list = []
    with open(archivo, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            fila = row[0]
            parte = fila.split('@')
            if parte[1] == 'gmail.com':
                email = Email.creaCuenta(fila)
                print(email)
                email_list.append(email)
            else:
                print('error en:' + fila)
    csvfile.close()
    return email_list
    