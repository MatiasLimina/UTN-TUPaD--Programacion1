#Gestión de turnos hospitalarios
nombre = input("Ingrese su nombre completo ").title()
dni = input("Ingrese su DNI sin puntos ")
len_dni = len(dni)
if len_dni != 11 :
    print ("Usted no ingreso un DNI válido")

edad = int(input("Ingrese su edad "))
obra_social = input("Tiene obra social?  SI / NO").upper()
prioridad = int(input("Prioridad médica: 1) Emergencia  2) Urgente  3) Control "))


