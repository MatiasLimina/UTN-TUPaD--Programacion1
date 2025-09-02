#Gestión de turnos hospitalarios
nombre = input("Ingrese su nombre completo ").title()
dni = input("Ingrese su DNI sin puntos ")
len_dni = len(dni)
if len_dni != 8 :
    print ("Usted no ingreso un DNI válido")

edad = int(input("Ingrese su edad "))
obra_social = input("Tiene obra social?  SI / NO ").upper()
prioridad = int(input("Prioridad médica: 1) Emergencia  2) Urgente  3) Control "))

print(f"Paciente: {nombre} \n DNI: {dni} \n Edad: {edad} \n Obra social: {obra_social} \n Nivel de prioridad: {prioridad}" )


if prioridad == 1 :
    print("Usted a sido asignado a la guardia")
elif prioridad == 2 :
    if obra_social == "SI" :
        print("Se le asignara un turno para dentro de menos de 24h")
    else:
        print("Se le asignara un turno para dentro de 48h")
else:
    if edad > 65 :
        print ("Usted recibira un turno dentro de las proximas 72h")
    else:
        print ("Usted recibira un turno dentro de los proximos 7 dias")

