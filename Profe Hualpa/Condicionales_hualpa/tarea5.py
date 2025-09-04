#Simulador de carrito de compras
nombre = input("Ingrese su nombre completo ").title()

pos_prod = False

while pos_prod == False:
    productos = int(input("Ingrese la cantidad de productos comprados "))
    if productos>0:
        pos_prod = True
    else:
        print ("No puede ingresar un número negativo de productos comprados")


