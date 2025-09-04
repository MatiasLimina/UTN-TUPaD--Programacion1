#Simulador de carrito de compras
nombre = input("Ingrese su nombre completo ").title()

pos_prod = False

while pos_prod == False:
    productos = int(input("Ingrese la cantidad de productos comprados "))
    if productos>0:
        pos_prod = True
    else:
        print ("No puede ingresar un número negativo de productos comprados")

monto_positivo = False
while monto_positivo == False:
    monto = float(input("Ingrese el monto total de la compra "))
    if monto > 0:
        monto_positivo=True
    else:
        print("No puede ingresar un monto negativo")

modo_pago = input("Ingrese el modo en el que va a pagar : efectivo  debito credito mercadopago").lower
efectivo = monto+monto*0.15
debito = monto+monto*0.10
credito = monto+monto*0.05
mercado_pago= monto +monto*0.20
importe_final = 0
if modo_pago == "efectivo":
    print(f"Usted recibira un descuento del {efectivo*100}")
    importe_final = monto - efectivo
elif modo_pago == "debito":
    importe_final = monto - debito
elif modo_pago == "credito":
    importe_final = monto + credito
elif modo_pago == "mercadopago":
    if monto > 10000:
        importe_final = monto - mercado_pago
    else:
        importe_final=monto

if productos>10:
    importe_final = importe_final - importe_final*0.05
    print (f"Usted compro un total de {productos}, por un monto de ${monto} \n Su metodo de pago elegido es {modo_pago}, El importe final luego de aplicarsele un descuente del {}")

