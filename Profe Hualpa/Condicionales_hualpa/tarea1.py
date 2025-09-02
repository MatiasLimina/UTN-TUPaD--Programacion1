#Clasificacion de impuestos
nombre = input("Ingrese su nombre completo ")
edad =int(input("Ingrese su edad ")) 
ingresos_anual =float(input("Indique sus ingresos anuales ")) 
impuesto_final = 0
print(f"Cliente: {nombre.title()} \n Edad: {edad} \n Ingresos anuales: ${ingresos_anual} ")

if ingresos_anual < 500000:
    print("Usted no debe pagar impuestos")
elif ingresos_anual >= 500000 and ingresos_anual < 2000000 :
    impuesto_final = ingresos_anual * 0.10
    print(f"Usted debe pagar un 10% de impuestos, el total a pagar sera de ${impuesto_final}")
elif ingresos_anual >= 2000000 and ingresos_anual < 5000000 :
    impuesto_final = ingresos_anual * 0.20
    print(f"Usted debe pagar un 20% de impuestos, el total a pagar sera de ${impuesto_final}")
elif ingresos_anual >= 5000000 :
    impuesto_final = ingresos_anual * 0.35
    print(f"Usted debe pagar un 35% de impuestos, el total a pagar sera de ${impuesto_final}")

if edad > 65 :
    impuesto_final = impuesto_final / 2
    print (f"Por su edad, se le aplica una reducción del 50%, su total a pagar final es de ${impuesto_final}")

