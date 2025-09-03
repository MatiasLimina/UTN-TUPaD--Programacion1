#Simulador de cajero automático
nombre = input("Ingrese su nombre completo ").title()
intentos = 0
pin = "1234"
while intentos != 3:
    inp_pin = input("Ingrese su PIN ")
    print(f"Numero de intentos {intentos}")
    if inp_pin != pin:
        print(f"Ingrese un PIN incorrecto, lleva {intentos+1} intentos")
        intentos += 1
    elif inp_pin == pin:
        print("PIN ingresado correctamente")
        break
if intentos == 3:
    print("Usted supero la cantidad de intentos permitidos, acceso denegado")