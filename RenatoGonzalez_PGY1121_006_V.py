import numpy as np

depa = np.array([
    [['','A','A10','3.800 UF',''],['','B','B10','3.000 UF',''],['','C','C10','2.800 UF',''],['','D','D10','3.500 UF','']],
    [['','A','A09','3.800 UF',''],['','B','B09','3.000 UF',''],['','C','C09','2.800 UF',''],['','D','D09','3.500 UF','']],
    [['','A','A08','3.800 UF',''],['','B','B08','3.000 UF',''],['','C','C08','2.800 UF',''],['','D','D08','3.500 UF','']],
    [['','A','A07','3.800 UF',''],['','B','B07','3.000 UF',''],['','C','C07','2.800 UF',''],['','D','D07','3.500 UF','']],
    [['','A','A06','3.800 UF',''],['','B','B06','3.000 UF',''],['','C','C06','2.800 UF',''],['','D','D06','3.500 UF','']],
    [['','A','A05','3.800 UF',''],['','B','B05','3.000 UF',''],['','C','C05','2.800 UF',''],['','D','D05','3.500 UF','']],
    [['','A','A04','3.800 UF',''],['','B','B04','3.000 UF',''],['','C','C04','2.800 UF',''],['','D','D04','3.500 UF','']],
    [['','A','A03','3.800 UF',''],['','B','B03','3.000 UF',''],['','C','C03','2.800 UF',''],['','D','D03','3.500 UF','']],
    [['','A','A02','3.800 UF',''],['','B','B02','3.000 UF',''],['','C','C02','2.800 UF',''],['','D','D02','3.500 UF','']],
    [['','A','A01','3.800 UF',''],['','B','B01','3.000 UF',''],['','C','C01','2.800 UF',''],['','D','D01','3.500 UF','']]
])

clientes = list()

def menu():
    opc = 0
    while opc == 0:
        try:
            opc = int(input('''
======== Casa Feliz =========
1. Comprar Departamentos
2. Departamentos Disponibles
3. Listado Compradores
4. Mostrar Ganancias
5. Salir
=============================
Ingrese una Opcion: '''))
            if opc < 0 or opc > 5:
                print("\n<< Favor ingresar un dato valido >>\n")
                opc = 0
            elif opc == 5:
                print("\nGracias por utilizar nuestra aplicacion!!\nEsperamos verte pronto!!")
                break
        except ValueError:
            print("\n<< Favor ingresar un dato valido >>\n")
            opc = 0
    return opc

def disponibleDepa():
    a = 0
    disponibles = 40
    print("Piso | A | B | C | D")
    for l in range(10):
        a+=1
        print()
        print(a,"   ",end=" ")
        for c in range(4):
            print(f"{depa[l][c][0] if depa[l][c][0] else '[ ]'}", end=" ")
            if depa[l][c][0] == 'X':
                disponibles -= 1
    print("\nDepartamentos disponibles:",disponibles)

def capturaRow():
    row = 0
    while row == 0:
        try:
            row = int(input("Ingrese el numero de Fila [0-9]: "))
        except ValueError:
            print("\n<< Favor ingresar un dato valido >>\n")
            row = 0
    return row

def capturaColumn():
    column = 0
    while column == 0:
        try:
            column = int(input("Ingrese el numero de Columna [0-9]: "))
        except ValueError:
            print("\n<< Favor ingresar un dato valido >>\n")
            column = 0
    return column

def comprarDepa(row,column,client):
    if (depaLibre(row,column)):
        depa[row][column][0] = '[X]'
        depa[row][column][4] = client
        return True
    else:
        return False

def depaLibre(row,column):
    if depa[row][column][0] == '':
        return True
    else:
        return False

def datosClient():
    client = 0
    while client == 0:
        try:
            client = int(input("Ingrese su Rut [sin Puntos ni Guion ni Digito Verificador]: "))
        except ValueError:
            print("\n<< Favor ingresar un dato valido >>\n")            
            client = 0
    return client

def addClient(client):
    clientes.append(client)

def listComprador():
    print("Lista de compradores:",clientes)

def start():
    startKey = 0
    while startKey != 5:
        startKey = menu()
        if startKey == 1:
            row = capturaRow()
            column = capturaColumn()
            rut = datosClient()
            comprarDepa(row,column,rut)
            addClient(rut)
        elif startKey == 2:
            disponibleDepa()
        elif startKey == 3:
            listComprador()
        elif startKey == 4:
            print

start()