#Evaluación de crédito bancario
nombre = input("Ingrese su nombre completo ")
cuit = input("Ingrese su CUIT")

if cuit[2] != "-" or cuit[11] != "-":
    print ("Ingrese un CUIT válido")

