import csv
import os

NOMBRE_ARCHIVO = "habitaciones.csv"
CAMPOS = ["habitacion", "estado"]

def inicializar_archivo():
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="") as f:
            escritor = csv.DictWriter(f, fieldnames=CAMPOS)
            escritor.writeheader()

def cargar_datos():
    inicializar_archivo()
    hotel = []
    with open(NOMBRE_ARCHIVO, "r") as archivo:
        lector = csv.DictReader(archivo, fieldnames=CAMPOS)
        next(lector)
        for fila in lector:
            try:
                habitacion = int(fila["habitacion"])
                if int(fila["estado"]) != 1 and int(fila["estado"]) != 0:
                    raise ValueError
                estado = int(fila["estado"])
                hotel.append({"habitacion":habitacion, "estado": estado})
            except ValueError:
                print("Dato invalido.")
    return hotel

def actualizar_datos(hotel):
    with open(NOMBRE_ARCHIVO, 'w', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(hotel)

def mostrar_menu():
    print('\n --- MENU ---')
    print('1- Mostrar habitaciones.')
    print('2- Agregar habitaciones.') #Agregar x valores
    print('3- Editar estado.')
    print('4- Eliminar habitacion.')
    print('5- Mostrar disponibles.')
    print('6- Agregar 1 habitación.') #Agrega 1 valor
    print('7- Reservar / liberar.')
    print('8- Salir.')
    print('9- Inicializar archivo.') #Inicializa

def mostrar_habitaciones(hotel):
    if not hotel:
        return 'No hay habitaciones existentes.'
    retorno = ''
    for hab in hotel:
        retorno += f'\n- Habitación: {hab['habitacion']} - {'Libre' if hab['estado'] == 0 else 'Ocupada'}'
    return retorno

def actualizar_estado(hotel):
    if not hotel:
        print('No hay habitaciones existentes.')
        return hotel
    while True:
        try:
            habitacion_act = int(input('Ingrese el número de la habitación a actualizar: '))
            for hab in hotel:
                if habitacion_act == hab['habitacion']:
                    print('Habitacion encontrada.')
                    estado_nvo = None
                    while(estado_nvo != 0 and estado_nvo != 1):
                        estado_nvo = int(input('Ingrese el estado de la habitación:\n1- Ocupada\n0- Libre\nOpcion: '))
                    hab['estado'] = estado_nvo
            print('Habitación actualizada.')
            actualizar_datos(hotel)
            return hotel
        except ValueError:
            print('Ingreso erróneo, tiene que ingresar un número.')
            
def eliminar_habitacion(hotel):
    if not hotel:
        return hotel
    hotel_nvo = []
    try:
        nro_hab = int(input('Ingrese el número de la habitación a eliminar: '))
        for hab in hotel:
            if nro_hab == hab['habitacion']:
                continue
            hotel_nvo.append(hab)
        print('Habitación eliminada.')
        actualizar_datos(hotel_nvo)
        return hotel_nvo
    except ValueError:
        print('Ingrese un número.')
        
def mostrar_disponibles(hotel):
    if not hotel:
        print('No hay habitaciones existentes.')
    else:
        print('- Habitaciones disponibles -')
        for hab in hotel:
            if (hab['estado'] == 0):
                print(f'- Habitación {hab['habitacion']}')
                
def agregar_habitacion(hotel):
    while True:
        try:
            # nva_hab = int(input('Ingrese el número de la nueva habitación: '))
            nro_nvo_hab = hotel[-1]['habitacion'] + 1
            hotel.append({'habitacion':nro_nvo_hab, 'estado':0})
            print('Habitacion agregada.')
            actualizar_datos(hotel)
            return hotel
        except ValueError:
            print('Dato erróneo. Debe ingresar un número entero.')

def reservar_liberar(hotel):
    if not hotel:
        print('No hay habitaciones existentes.')
        return hotel
    while True:
        try:
            habitacion_act = int(input('Ingrese el número de la habitación a actualizar: '))
            for hab in hotel:
                if habitacion_act == hab['habitacion']:
                    print(f'Habitacion encontrada. Esta habitación está {'libre' if hab['estado'] == 0 else 'ocupada'}')
                    hab['estado'] = 0 if hab['estado'] == 1 else 1
            print('Habitación actualizada.')
            actualizar_datos(hotel)
            return hotel
        except ValueError:
            print('Ingreso erróneo, tiene que ingresar un número.')

def agregar_habitaciones(hotel):
    #datos_nvo = []
    while True:
        try:
            cantidad = int(input('¿Cuantas habitaciones quiere agregar? '))
            for i in range(cantidad):
                nro_nvo_hab = hotel[-1]['habitacion'] + 1
                hotel.append({'habitacion':nro_nvo_hab, 'estado':0})
                #datos_nvo.append({'habitacion':nro_nvo_hab, 'estado':0})
            print('Habitaciones agregadas.')
            #agregar_multiples_datos(datos_nvo)
            actualizar_datos(hotel)
            return hotel
        except ValueError:
            print('Dato erróneo. Debe ingresar un número entero.')

# FUNCION SI QUIERO AGREGAR DIRECTO AL ARCHIVO
def agregar_multiples_datos(datos_nvos):
    with open(NOMBRE_ARCHIVO, 'a', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writerows(datos_nvos)