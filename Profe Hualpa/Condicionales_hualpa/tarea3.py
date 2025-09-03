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
retiro = 0
cancelar = "no"
saldo_inicial = 50000
while cancelar == "no":
    monto = float(input("Ingrese el monto a retirar"))
    if monto > saldo_inicial:
        while monto > saldo_inicial:
            print (f"Usted ingreso un monto que supera el saldo disponible de ${saldo_inicial}")
            monto = float(input("Ingrese el monto a retirar"))
    
    if monto % 1000 == 0 and monto >= 20000:
        retiro = monto + monto*0.02
        saldo_inicial = saldo_inicial - retiro
        print (f"Usted retirara ${retiro}, al tratarse de un monto superior a $20000 se le aplicara una comisión del 2% \n Su saldo restante es de: ${saldo_inicial}")
    elif monto % 1000 != 0:
        print ("Ingreso un monto inválido")
    else:
        retiro = monto
        saldo_inicial = saldo_inicial - retiro
        print(f"Usted retirara ${retiro} \n Su saldo restante es de: ${saldo_inicial}")
    cancelar = input("Desea cancelar la operación: si/no ").lower()

print ("Gracias por operar con nosotros!")
