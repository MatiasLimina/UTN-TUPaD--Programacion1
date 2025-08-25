fecha:str = input("Ingrese la fecha: ")
print(fecha)

dia = fecha.split(",")
dia = dia[0]
dia = dia.lower()
print(dia)

DD = fecha.split(",")
DD = DD[1]
DD = (DD)
print(DD)

DD = DD.split("/")
MM = DD[1]
MM = (MM)

DD = (DD[0])
DD = DD.strip()
print (DD,MM)

if dia.isalpha(): 
    print ("Es valido")
else:
    print("Invalido")

if DD.isnumeric():
    print("Es numero")
else:
    print("No es num")

if MM.isnumeric():
    print("Es numero")
else:
    print("No es num")

DD = int(DD)
MM = int(MM)
dia_semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

if not dia in dia_semana:
    print("Ingrese un dia valido")

if DD>0 and DD<=31:
    print("Fecha valida")

if MM>0 and MM<=12:
    print("Mes valido")

if dia == ("lunes" or "martes" or "miercoles" ):
    examenes = input("Se realizaron examenes? ")
    examenes = examenes.lower()
    if examenes == "si":
        cant_aprobados = int(input("Ingrese la cantidad de alumnos que aprobaron: "))
        cant_desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
        total_alumnos = cant_aprobados + cant_desaprobados
        porcentaje_aprob = (cant_aprobados/total_alumnos)*100
        print(f"El porcentaje de alumnos aprobados es de %{porcentaje_aprob}.")

if dia == "jueves":
    porcentaje_asist = int (input("Ingrese el procentaje de asistencia a su clase: "))
    if porcentaje_asist > 50:
        print("Asistio la mayoria")
    else:
        print("No asistio la mayoria")

if dia == "viernes":
    if (DD == 1 and MM==1) or (DD == 1 and MM == 7):
        print("Comienzo de nuevo ciclo")
        nuevos_alumnos = int(input("Ingrese cant de nuevos alumnos: "))
        arancel = int(input("Ingrese el arancel de los nuevos alumnos: "))
        total_ganancia= nuevos_alumnos*arancel
        print (f"Las ganancias totales por nuevos alumnos es de ${total_ganancia}")
