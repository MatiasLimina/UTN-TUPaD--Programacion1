#Gestión de turnos hospitalarios
nombre = input("Ingrese su nombre completo").title()
dni = input("Ingrese su DNI sin puntos")
len_dni = len(dni)
if len_dni != 11 :
    print ("Usted no ingreso un DNI válido")

