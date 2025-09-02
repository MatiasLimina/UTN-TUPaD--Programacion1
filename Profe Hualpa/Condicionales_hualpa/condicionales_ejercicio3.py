#Evaluación de crédito bancario
nombre = input("Ingrese su nombre completo ")
cuit = input("Ingrese su CUIT")

if cuit[2] != "-" or cuit[11] != "-":
    print ("Ingrese un CUIT válido")

ingresos = float(input("Indique sus ingresos mensuales "))
anti_laboral = int(input("Ingrese la cantidad de años correspondiente a su antiguedad laboral "))
hist_crediticio = input("Situacion crediticia:  bueno regular malo ").lower()

print(f"Cliente: {nombre.title()} \n CUIT: {cuit} \n Ingresos: ${ingresos} \n Antiguedad: {anti_laboral} \n Historial crediticio: {hist_crediticio}" )

if hist_crediticio == "malo":
    print ("Rechazado")
elif ingresos < 200000:
    print("Rechazado")
elif ingresos >= 200000 and anti_laboral < 2:
    print ("Usted puede pedir un maximo de $500.000")
elif ingresos >= 200000 and anti_laboral >= 2:
    if hist_crediticio == "regular":
        print("Puede pedir hasta $1.000.000")
    elif hist_crediticio == "bueno":
        print("Puede pedir hasta $3.000.000")

