import csv

def busqueda(archivo):
    with open(archivo, newline='') as csvfile:
        reader = csv.reader(csvfile)
        cont = 0
        dominio = input('ingrese dominio a buscar: ')
        for row in reader:
            fila = row[0]
            part = fila.split('@')
            part2 = part[1].split('.')
            if part2[0] == dominio:
                cont += 1
        print('Hay',cont,'email/s que coinciden con el dominio')
    csvfile.close()